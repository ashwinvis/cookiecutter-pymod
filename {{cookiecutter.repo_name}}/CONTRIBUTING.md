
Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues.

If you are reporting a bug, please include:

  - Your operating system name and version.
  - Any details about your local setup that might be helpful in
    troubleshooting.
  - Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and
"help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement
it.

### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation,
whether as part of the official {{ cookiecutter.project_name }} docs,
in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues.

If you are proposing a feature:

  - Explain in detail how it would work.
  - Keep the scope as narrow as possible, to make it easier to
    implement.
  - Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `{{ cookiecutter.project_name }}` for local development.

1. Fork the `{{ cookiecutter.repo_name }}` repo on GitHub.
2. Clone your fork locally:

        $ git clone git@github.com:your_name_here/{{ cookiecutter.repo_name }}.git

3. Install your local copy into a virtual environment. This is how you set up your fork for local development:

        $ python -m venv venv
        $ source venv/bin/activate
        $ cd {{ cookiecutter.repo_name }}/
        $ pip install -e '.[dev]'

4. Create a branch for local development:

        $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the linters.
   This is handled automatically using pre-commit. Install the pre-commit git
   hooks as follows:

        $ pre-commit install

    To run the unit tests in your current environment:

        $ pytest

    You can also run the tests in a separate environment with multiple Python versions using:

        $ tox

6. Commit your changes and push your branch to GitHub:

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

7.  Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and for PyPy. Check
   https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pull_requests
   and make sure that the tests pass for all supported Python versions.

## Tips

To run a subset of tests:

    {% if cookiecutter.use_pytest == 'y' -%}
    $ py.test tests.test_{{ cookiecutter.project_slug }}
    {% else %}
    $ python -m unittest tests.test_{{ cookiecutter.project_slug }}
    {%- endif %}

## Deploying
A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.md).
Then run:

    $ git tag <insert version>
    $ git push
    $ git push --tags

{% if cookiecutter.use_pypi_deployment_with_travis == 'y' -%}
Travis will then deploy to PyPI if tests pass.
{% else -%}
To deploy:

    $ make dist-check
    $ make release

{%- endif %}
