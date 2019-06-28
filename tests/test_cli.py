#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `wdbreduce` package."""

from click.testing import CliRunner
from wdbreduce import cli
import os


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    basedir = os.path.dirname(__file__)
    inputdir = f"{basedir}/data/input"
    outputdir = f"{basedir}/data/output"
    result = runner.invoke(cli.main, [inputdir, outputdir])
    assert result.exit_code == 0
    expfile = f"{outputdir}/samer-bdy.txt"
    veriffile = f"{outputdir}/samer-bdy_verif.txt"
    assert(open(expfile).read() == open(veriffile).read())
    os.remove(expfile)
