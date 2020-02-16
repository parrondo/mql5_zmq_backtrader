#!/usr/bin/env python

"""Tests for `mql5_zmq_backtrader` package."""


import unittest
from click.testing import CliRunner

from mql5_zmq_backtrader import mql5_zmq_backtrader
from mql5_zmq_backtrader import cli


class TestMql5_zmq_backtrader(unittest.TestCase):
    """Tests for `mql5_zmq_backtrader` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'mql5_zmq_backtrader.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
