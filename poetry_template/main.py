import click


@click.command()
@click.argument("name")
@click.version_option()
def hello(name):
    """Print a greeting for NAME"""
    click.echo(f"Hello, {name}!")
