#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `wdbreduce/utils.py` package."""
import logging

from wdbreduce import utils


def test_count_to_log_level():
    assert utils.count_to_log_level(0) == logging.ERROR
    assert utils.count_to_log_level(1) == logging.WARNING
    assert utils.count_to_log_level(2) == logging.INFO
    assert utils.count_to_log_level(3) == logging.DEBUG
