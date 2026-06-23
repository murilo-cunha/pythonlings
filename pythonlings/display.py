import os

from rich.console import Console
from rich.layout import Layout
from rich.markdown import Markdown
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn
from rich.syntax import Syntax
from rich.text import Text

console = Console()

COMPACT_HEIGHT = 20


def build_layout(
    exercise,
    current: int,
    total: int,
    watching: bool,
    hint_text=None,
    height=None,
    exercise_label=None,
) -> Layout:
    if height is None:
        height = console.size.height
    compact = height < COMPACT_HEIGHT

    layout = Layout()
    sections = [Layout(name="header", size=1 if compact else 3)]
    if not compact:  # code panel only when there's vertical room
        sections.append(Layout(name="code", ratio=2, minimum_size=3))
    sections.append(Layout(name="status", ratio=2, minimum_size=3))  # feedback — always
    if hint_text:
        # smaller floor in compact so a tiny pane still keeps the footer visible
        sections.append(Layout(name="hint", ratio=1, minimum_size=3 if compact else 4))
    sections.append(Layout(name="footer", size=1 if compact else 3))
    layout.split_column(*sections)

    # Header: exercise counter + progress bar
    progress = Progress(
        TextColumn("[bold]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
        expand=True,
    )
    desc = f"Exercise {current}/{total}"
    if exercise_label:
        desc += f" - {exercise_label}"
    progress.add_task(desc, total=total, completed=current)
    if compact:
        layout["header"].update(progress)
    else:
        layout["header"].update(Panel(progress, border_style="bright_black"))

    # Code panel: syntax-highlighted source (full mode only)
    if not compact:
        try:
            with open(exercise.fp) as f:
                source = f.read()
        except Exception:
            source = ""
        syntax = Syntax(source, "python", theme="github-dark", line_numbers=True)
        layout["code"].update(
            Panel(syntax, title=os.path.basename(exercise.fp), border_style="bright_black")
        )

    # Status panel
    if exercise.to_do:
        status_color = "yellow"
        status_body = Text("[MAKE IT PASS]", style="bold yellow")
    elif exercise.error:
        status_color = "red"
        output_text = exercise.output or ""
        status_body = Text.assemble(
            ("[ERROR]\n", "bold red"),
            (output_text, "default"),
        )
    else:
        status_color = "green"
        status_body = Text("[SUCCESS]", style="bold green")
    layout["status"].update(Panel(status_body, title="Status", border_style=status_color))

    # Hint panel (only when toggled on)
    if hint_text:
        layout["hint"].update(Panel(Markdown(hint_text), title="Hint", border_style="yellow"))

    # Footer: keyboard hints + optional spinner
    hint_label = "h to hide hint" if hint_text else "h for hint"
    if compact:
        text = f"Ctrl+C quit · {hint_label}"
        if watching:
            text += " · ⠸ watching"
        layout["footer"].update(Text.from_markup(f"[dim]{text}[/dim]"))
    elif watching:
        layout["footer"].update(Panel(Text.from_markup(
            f"[dim]Ctrl+C to quit  │  [bold]{hint_label}[/bold]\n"
            "⠸ Watching for changes…[/dim]"
        ), border_style="bright_black"))
    else:
        layout["footer"].update(Panel(Text.from_markup(
            f"[dim]Ctrl+C to quit  │  [bold]{hint_label}[/bold][/dim]"
        ), border_style="bright_black"))

    return layout
