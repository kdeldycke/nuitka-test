from click import command, echo


@command()
def my_cli():
    echo("Hello world!")
