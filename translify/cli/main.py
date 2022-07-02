import click

@click.command()
@click.option("--text", "-t", default=None, help="Text to be translated")
@click.option("--file", "-f", default=None, help="File to be read from")
# TODO: Add file encoding option
@click.option("--lang", "-l", help="Language of the text", required=True)
# TODO: Add a --version option
# TODO: Add a length of summary option
def cli(text, file, lang):
    """A tool to interpret text in a language other than English to summarize it in English."""
    # Possibly allow the tool/utility to simply summarize a text in English
    if text:
        click.echo("OMG there is some text.")
    elif file:
        click.echo("OML there is a file.")
    else:
        raise click.UsageError("Neither text nor file parameters have been provided")


if __name__ == "__main__":
    # Remove when publishing as a package using setuptools
    cli()