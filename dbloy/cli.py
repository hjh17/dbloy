import click


from dbloy.util import CONTEXT_SETTINGS
from dbloy.version import print_version_callback, version
from dbloy.configure.cli import configure
from dbloy.apply.cli import apply

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--version', '-v', is_flag=True, callback=print_version_callback,
              expose_value=False, is_eager=True, help=version)
def cli():
    pass


cli.add_command(configure, name='configure')
cli.add_command(apply, name='apply')

if __name__ == "__main__":
    cli()
