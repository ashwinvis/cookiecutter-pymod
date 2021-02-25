# Cookiecutter PyPack

[![Updates](https://pyup.io/repos/github/ashwinvis/cookiecutter-pypack/shield.svg)](https://pyup.io/repos/github/ashwinvis/cookiecutter-pypack/)
[![Travis build status](https://travis-ci.org/ashwinvis/cookiecutter-pypack.svg?branch=master)](https://travis-ci.org/ashwinvis/cookiecutter-pypack)
[![Actions build Status](https://github.com/ashwinvis/cookiecutter-pypack/workflows/Python%20package/badge.svg)](https://github.com/ashwinvis/cookiecutter-pypack/actions)
[![Windows build status on
Appveyor](https://ci.appveyor.com/api/projects/status/github/ashwinvis/cookiecutter-pypack?branch=master&svg=true)](https://ci.appveyor.com/project/ashwinvis/cookiecutter-pypack/branch/master)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
**Py**thon **pack**age with some modern twists:

  - Primarily uses
    [setup.cfg](https://setuptools.readthedocs.io/en/latest/setuptools.html?highlight=setup.cfg#configuring-setup-using-setup-cfg-files)
    for storing packaging metadata instead of relying on
    `setup.py` too much.
  - Relies on [src](https://hynek.me/articles/testing-packaging/) layout
    for the package.
  - Support `setuptools_scm` versioning for development.
  - Uses [pre-commit hooks](https://pre-commit.com/hooks.html) to enforce code-style.
  - Uses markdown for the `README.md` etc. instead of reStructured Text.
  - Allows project name, repo name and package name to be different (for
    e.g. having something like "Scikit Learn", `scikit-learn` and
    `sklearn` respectively).
  - Adds optional support for either an `argparse` based command-line
    tool, or a `Click` based one (only the latter was available in the
    original template).
  - By default `python_requires>=3.6` is preferred, since new packages
    should be able to use
    [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals).

**TLDR:** you get this:

``` shell
$ tree --dirsfirst -a pypack/
pypack/
├── docs
│   └── ...
├── .github
│   ├── workflows
│   │   └── tests.yml
│   └── ISSUE_TEMPLATE.md
├── src
│   └── pypack
│       ├── cli.py
│       ├── __init__.py
│       └── pypack.py
├── tests
│   └── ...
├── CONTRIBUTING.md
├── .editorconfig
├── .git
├── .gitignore
├── HISTORY.md
├── LICENSE
├── Makefile
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── setup.cfg
├── setup.py
├── THANKS.md
├── tox.ini
└── .travis.yml
```

## See Also

  - GitHub repo: <https://github.com/ashwinvis/cookiecutter-pypack/>
  - Documentation: <https://cookiecutter-pypackage.readthedocs.io/>
  - Free software: BSD license

## Features

  - Testing setup with `unittest` and `python setup.py test` or
    `py.test`
  - [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous
    Integration testing
  - [Tox](http://tox.readthedocs.io) testing: Setup to easily test for
    Python 3.6+
  - [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for
    generation with, for example, [ReadTheDocs](https://readthedocs.io/)
  - Auto-release to [PyPI](https://pypi.python.org/pypi) when you push a
    new tag to master (optional)
  - Command line interface using Click (optional)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this
requires Cookiecutter 1.4.0 or higher):

    pip install -U cookiecutter

Generate a Python package project:

    cookiecutter gh:ashwinvis/cookiecutter-pypack

Then:

  - Create a repo and put it there.
  - Add the repo to your [Travis-CI](http://travis-ci.org/) account.
  - Install the package into a virtualenv. (`pip install -e '.[dev]'` or
    `make develop`)
  - [Register](https://packaging.python.org/distributing/#register-your-project)
    your project with PyPI.
  - Run the Travis CLI command `travis encrypt
    --add deploy.password` to encrypt your PyPI password in Travis
    config and activate automated deployment on PyPI when you push a new
    tag to master branch.
  - Add the repo to your [ReadTheDocs](https://readthedocs.io/) account
    + turn on the ReadTheDocs service hook.
  - Release your package by pushing a new tag to master.
  - Add a `requirements.txt` file that
    specifies the packages you will need for your project and their
    versions. For more info see the [pip docs for requirements
    files](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
  - Activate your project on [pyup.io](https://pyup.io/).

For more details, see the [cookiecutter-pypackage
tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html).

## Not Exactly What You Want?

Don't worry, you have options:

### Similar Cookiecutter Templates

  - [ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary): Another template which uses the `src/` layout
  - [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage):
    The original cookiecutter template.
  - Also see the
    [network](https://github.com/ashwinvis/cookiecutter-pypack/network)
    and [family
    tree](https://github.com/ashwinvis/cookiecutter-pypack/network/members)
    for this repo. (If you find anything that should be listed here,
    please add it and send a pull request\!)

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork
this to create your own version. Or create your own; it doesn't strictly
have to be a fork.

  - Once you have your own version working, add it to the Similar
    Cookiecutter Templates list above with a brief description.
  - It's up to you whether or not to rename your fork/own version. Do
    whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if
they make my own packaging experience better.
