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
    import select, tty, termios
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


def observe_exercise_until_pass(exercise: Exercise, live: Live, current: int, total: int) -> None:
    modified_event = threading.Event()
    hint_event = threading.Event()
    stop_event = threading.Event()
    hint_text = None

    def _fire(event):
        modified_event.set()

    handler = PatternMatchingEventHandler(patterns=["*.py"], ignore_directories=True)
    handler.on_modified = _fire
    handler.on_created  = _fire
    handler.on_moved    = _fire
    observer = Observer()
    observer.schedule(handler, os.path.dirname(exercise.fp), recursive=False)
    observer.start()
    kb_thread = _start_keyboard_listener(hint_event, stop_event)
    try:
        while True:
            if hint_event.is_set() and hint_text is None:
                hint_text = _get_hint_text(exercise)
            live.update(build_layout(exercise, current, total, watching=True, hint_text=hint_text))
            if modified_event.wait(timeout=0.5):
                modified_event.clear()
                exercise.is_not_done()
                exercise.process()
                live.update(build_layout(exercise, current, total, watching=False, hint_text=hint_text))
                if not exercise.error and not exercise.to_do:
                    break
    finally:
        stop_event.set()
        if kb_thread is not None:
            kb_thread.join(timeout=0.5)
        observer.stop()
        observer.join()


def process_exercises() -> None:
    fps = walk_exercises()
    total = len(fps)
    with Live(console=console, screen=True, refresh_per_second=4) as live:
        for idx, fp in enumerate(fps, 1):
            exercise = Exercise(fp)
            exercise.process()
            live.update(build_layout(exercise, idx, total, watching=False))
            if exercise.error or exercise.to_do:
                observe_exercise_until_pass(exercise, live, idx, total)


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
