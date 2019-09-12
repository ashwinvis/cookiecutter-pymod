{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Travis build status](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
[![Actions build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/Python%20package/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions)
[![Documentation status](https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest)](https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}

* Free software: {{ cookiecutter.open_source_license }}

* Documentation: https://{{ cookiecutter.repo_name }}.readthedocs.io.
{% endif %}

## Installation

    pip install {{ cookiecutter.project_slug }}

## Features

* TODO

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[ashwinvis/cookiecutter-pypack](https://github.com/ashwinvis/cookiecutter-pypack)
project template.
