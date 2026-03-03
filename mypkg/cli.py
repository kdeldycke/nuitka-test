"""Simple Click CLI."""

import click


@click.command()
@click.version_option("1.0.0")
def hello():
    """Say hello."""
    click.echo("Hello from mypkg!")
