from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn
from rich.syntax import Syntax
from rich.text import Text

console = Console()


def build_layout(exercise, current: int, total: int, watching: bool) -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="code"),
        Layout(name="status"),
        Layout(name="footer", size=3),
    )

    # Header: exercise counter + progress bar
    progress = Progress(
        TextColumn("[bold]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    )
    task_id = progress.add_task(f"Exercise {current} of {total}", total=total, completed=current)
    layout["header"].update(Panel(progress, border_style="bright_black"))

    # Code panel: syntax-highlighted source
    try:
        with open(exercise.fp) as f:
            source = f.read()
    except Exception:
        source = ""
    syntax = Syntax(source, "python", theme="github-dark", line_numbers=True)
    layout["code"].update(Panel(syntax, title=exercise.fp, border_style="bright_black"))

    # Status panel
    if exercise.to_do:
        status_color = "yellow"
        status_label = "[MAKE IT PASS]"
        status_body = Text(status_label, style="bold yellow")
    elif exercise.error:
        status_color = "red"
        status_label = "[ERROR]"
        output_text = exercise.output or ""
        status_body = Text.assemble(
            (status_label + "\n", "bold red"),
            (output_text, "default"),
        )
    else:
        status_color = "green"
        status_label = "[SUCCESS]"
        status_body = Text(status_label, style="bold green")

    layout["status"].update(Panel(status_body, title="Status", border_style=status_color, height=12))

    # Footer: keyboard hints + optional spinner
    if watching:
        layout["footer"].update(Panel(Text.from_markup(
            "[dim]Ctrl+C to quit  │  [bold]pythonlings hint[/bold] for a hint\n"
            "⠸ Watching for changes…[/dim]"
        ), border_style="bright_black"))
    else:
        layout["footer"].update(Panel(Text.from_markup(
            "[dim]Ctrl+C to quit  │  [bold]pythonlings hint[/bold] for a hint[/dim]"
        ), border_style="bright_black"))

    return layout
