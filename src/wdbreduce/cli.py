# -*- coding: utf-8 -*-
"""Console script for wdbreduce."""
import sys
import click
import logging

from wdbreduce.utils import count_to_log_level
from wdbreduce.wdbreduce import RdpPolygonReducer

__version__ = '0.1.0'


@click.command()
@click.argument('inputdir')
@click.argument('outputdir')
@click.option(
    '--epsilon',
    '-e',
    default=0.003,
    help="tolerance in deg when reducing the polygon. 0.001 deg corresponds to 111.1m resolution at Equator")
@click.option(
    '--dry-run',
    '-n',
    flag_value='dry_run',
    default=False,
    help="Perform a trial run with no changes made")
@click.option(
    '--verbose',
    '-v',
    count=True,
    help="Increase verbosity (specify multiple times for more)")
@click.option('--version', '-V', is_flag=True, help="Print version")
def main(*args, **kwargs):
    """Console script for test_cli_project."""

    logging.basicConfig(level=count_to_log_level(kwargs['verbose']))

    logging.warning("This is a warning.")
    logging.info("This is an info message.")
    logging.debug("This is a debug message.")

    if kwargs['version']:
        click.echo(__version__)
        return 0

    if kwargs['dry_run']:
        click.echo("Is dry run")
        return 0

    click.echo(
        "Replace this message by putting your code into test_cli_project.cli.main"
    )
    click.echo("See click documentation at http://click.pocoo.org/")

    inputdir  = kwargs["inputdir"]
    outputdir = kwargs["outputdir"]
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    infiles = glob.glob(inputdir+"/*.txt")
    for infile in infiles:
        outfile = outputdir+"/"+os.path.basename(infile)
        print("infile: {:s}, outfile: {:s}".format(infile,outfile))
        red = RdpPolygonReducer(infile,outfile)
        red.readAndReduce(epsilon)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
