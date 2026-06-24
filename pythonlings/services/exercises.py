import os
import re
import sys
import threading

import i18n
from rich.live import Live
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from pythonlings.display import build_layout, console
from pythonlings.domain.exercises import Exercise

try:
    import select
    import termios
    import tty

    _TTY_AVAILABLE = True
except ImportError:
    _TTY_AVAILABLE = False

_ = i18n.t


def get_exercises_root() -> str:
    path = os.path.join(os.getcwd(), "pythonlings", "exercises")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Path: {path} does not exist. "
            "Are you running Pythonlings in repository root?"
        )
    return path


def walk_exercises():
    root = get_exercises_root()
    fps = []
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d != 'tests')
        for fname in sorted(files):
            if fname.endswith(".py") and not fname.startswith("test_"):
                fps.append(os.path.join(dirpath, fname))
    return fps


def _start_keyboard_listener(hint_event: threading.Event, stop_event: threading.Event):
    if not _TTY_AVAILABLE:
        return None
    def _listen():
        fd = sys.stdin.fileno()
        try:
            old = termios.tcgetattr(fd)
        except termios.error:
            return
        try:
            tty.setcbreak(fd)
            while not stop_event.is_set():
                r, _, _ = select.select([sys.stdin], [], [], 0.1)
                if r:
                    ch = sys.stdin.read(1)
                    if ch.lower() == 'h':
                        hint_event.set()
        except Exception:
            pass
        finally:
            try:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            except Exception:
                pass
    t = threading.Thread(target=_listen, daemon=True)
    t.start()
    return t


def _get_hint_text(exercise) -> str:
    return i18n.t(f'{exercise.package}.{exercise.name}')


def _first_failing(fps, cache):
    """Return (1-based index, processed Exercise) of the first failing exercise,
    or (None, None) when every exercise passes.

    `cache` maps realpath(fp) -> passed(bool). A cached True means the exercise
    passed when its file was last seen and has not changed since, so it is
    skipped; anything else is (re)processed and the result cached. The freshly
    processed Exercise that is returned already has its `.output` populated for
    rendering.
    """
    for idx, fp in enumerate(fps, 1):
        key = os.path.realpath(fp)
        if cache.get(key) is True:
            continue
        ex = Exercise(fp)
        ex.process()
        passed = (not ex.error) and (not ex.to_do)
        cache[key] = passed
        if not passed:
            return idx, ex
    return None, None


def _completion_panel():
    from rich.align import Align
    from rich.panel import Panel
    from rich.text import Text
    body = Align.center(
        Text("🎉 All exercises complete!", style="bold green"),
        vertical="middle",
    )
    return Panel(body, title="Pythonlings", border_style="green")


def process_exercises() -> None:
    """Watch the exercises tree and always display the first failing exercise.

    Stateless and always-sequential: the "current" exercise is recomputed from
    the start on every change, so reverting an earlier exercise drops back to
    it and fixing it walks forward again. Nothing is persisted; an in-memory
    cache only skips exercises proven to pass since their file last changed.
    """
    fps = walk_exercises()
    total = len(fps)
    root = get_exercises_root()

    cache = {}                       # realpath(fp) -> passed(bool); in-memory only
    changed_paths = set()
    lock = threading.Lock()
    modified_event = threading.Event()
    hint_event = threading.Event()
    stop_event = threading.Event()

    def _record(path):
        if path:
            with lock:
                changed_paths.add(os.path.realpath(path))
                modified_event.set()

    def _on_event(event):
        _record(getattr(event, "src_path", None))
        _record(getattr(event, "dest_path", None))   # on_moved supplies a destination

    handler = PatternMatchingEventHandler(patterns=["*.py"], ignore_directories=True)
    handler.on_modified = _on_event
    handler.on_created  = _on_event
    handler.on_moved    = _on_event
    observer = Observer()
    observer.schedule(handler, root, recursive=True)
    observer.start()
    kb_thread = _start_keyboard_listener(hint_event, stop_event)

    try:
        with Live(console=console, screen=True, refresh_per_second=4) as live:
            idx, current = _first_failing(fps, cache)
            hint_visible = False
            while True:
                if current is None:
                    live.update(_completion_panel())
                    break
                label = os.path.relpath(current.fp, root)
                shown = _get_hint_text(current) if hint_visible else None
                live.update(build_layout(current, idx, total, watching=True,
                                         hint_text=shown, exercise_label=label))
                if modified_event.wait(timeout=0.2):     # a watched .py actually changed
                    with lock:
                        changed = list(changed_paths)
                        changed_paths.clear()
                        modified_event.clear()
                    for p in changed:
                        cache.pop(p, None)               # re-check exactly what changed
                    prev_fp = current.fp
                    idx, current = _first_failing(fps, cache)
                    if current is not None and current.fp != prev_fp:
                        hint_visible = False             # reset hint when exercise changes
                elif hint_event.is_set():                # keypress, no file change
                    hint_event.clear()
                    hint_visible = not hint_visible
    finally:
        stop_event.set()
        if kb_thread is not None:
            kb_thread.join(timeout=0.5)
        observer.stop()
        observer.join()


def show_hint(exercise_name=None) -> None:
    if exercise_name is None:
        fps = walk_exercises()
        for fp in fps:
            ex = Exercise(fp)
            if ex.is_not_done() or (not ex.to_do and ex.error):
                exercise_name = ex.name
                package = ex.package
                break
        else:
            console.print("[green]All exercises complete![/green]")
            return
    else:
        package = re.sub(r'\d+$', '', exercise_name)

    from rich.markdown import Markdown
    from rich.panel import Panel
    hint_text = _(f'{package}.{exercise_name}')
    console.print(Panel(Markdown(hint_text), title=f"Hint: {exercise_name}", border_style="yellow"))
