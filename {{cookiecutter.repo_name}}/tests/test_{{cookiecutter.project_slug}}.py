#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

from warnings import warn
{% if cookiecutter.use_pytest == 'y' %}
import pytest
{% else -%}
import unittest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}

{%- if cookiecutter.use_pytest == 'y' %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/ashwinvis/cookiecutter-pypack')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_scm_version():
    """Test scm version."""
    if ".dev" in {{ cookiecutter.project_slug }}.__version__:
        warn("At some distance from the last tagged release")
    if {{ cookiecutter.project_slug }}.__version__[-8:].isdecimal():
        warn("Repository not clean, commit needed")

{%- if cookiecutter.command_line_interface|lower == 'click' %}

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Test something."""
        pass

    def test_scm_version(self):
        """Test scm version."""
        if ".dev" in {{ cookiecutter.project_slug }}.__version__:
            warn("At some distance from the last tagged release")
        if {{ cookiecutter.project_slug }}.__version__[-8:].isdecimal():
            warn("Repository not clean, commit needed")

{%- if cookiecutter.command_line_interface|lower == 'click' %}

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert "--help  Show this message and exit." in help_result.output
{%- endif %}
{%- endif %}
