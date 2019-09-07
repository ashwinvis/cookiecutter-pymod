# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""



__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"

try:
    from ._version import __version__
except ImportError:
    from pkg_resources import get_distribution
    __version__ = get_distribution(__package__).version
    del get_distribution
