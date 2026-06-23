import os

import click
import i18n

i18n.config.set("locale", os.getenv("PYTHONLINGS_LANGUAGE", "en"))
i18n.load_path.append("pythonlings/i18n")


@click.group()
def cli():
    pass


@cli.command()
def start():
    """Run exercises with file-watching."""
    from pythonlings.services.exercises import process_exercises
    process_exercises()


@cli.command()
@click.argument("exercise_name", required=False)
def hint(exercise_name):
    """Show the hint for the current (or named) exercise."""
    from pythonlings.services.exercises import show_hint
    show_hint(exercise_name)


def run():
    cli()
