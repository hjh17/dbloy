import subprocess

import click

from dbloy.util import CONTEXT_SETTINGS


@click.command(context_settings=CONTEXT_SETTINGS,
               short_help='Configures host and authentication info for the CLI.')
def configure():
    """Sets up authentication using authentication token. Credentials are stored at `~/.databrickscfg`."""
    subprocess.call(["databricks", "configure", "--token"])