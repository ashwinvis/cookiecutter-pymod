from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import yaml
import datetime
from cookiecutter.utils import rmtree
import pytest

from click.testing import CliRunner

import importlib


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    assert result.project is not None, "Cookiecutter failed to bake!"
    try:
        yield result
    finally:
        rmtree(str(result.project))


def yaml_load(text):
    """Safely load yaml text"""
    return yaml.load(text, Loader=yaml.SafeLoader)


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    assert result.project is not None, "Cookiecutter failed to bake!"
    project_path = str(result.project)
    # repo_name is by default different from project_slug
    project_slug = os.path.split(project_path)[-1].replace('-', '_')
    project_dir = os.path.join(project_path, 'src', project_slug)
    assert os.path.exists(project_dir), "project_dir missing from" + project_path
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'src' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'tests' in found_toplevel_files


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        run_inside_dir('tox -e py flake', str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_with_install_dist_check(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()

        def run_and_assert_success(cmd):
            assert run_inside_dir(cmd, str(result.project)) == 0, cmd + " failed"

        run_and_assert_success("make install")
        run_and_assert_success("make dist")
        run_and_assert_success('make dist-check')
        print("test_bake_with_install_dist_check path", str(result.project))


def test_bake_withspecialchars_and_run_tests(cookies):
    """Ensure that a `full_name` with double quotes does not break setup.py"""
    with bake_in_temp_dir(cookies, extra_context={'full_name': 'name "quote" name'}) as result:
        assert result.project.isdir()
        run_inside_dir('tox -e py', str(result.project)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    with bake_in_temp_dir(cookies, extra_context={'full_name': "O'connor"}) as result:
        assert result.project.isdir()
        run_inside_dir('tox -e py', str(result.project)) == 0


# def test_bake_and_run_travis_pypi_setup(cookies):
#     # given:
#     with bake_in_temp_dir(cookies) as result:
#         project_path = str(result.project)
#
#         # when:
#         travis_setup_cmd = ('python travis_pypi_setup.py'
#                             ' --repo ashwinvis/cookiecutter-pypack --password invalidpass')
#         run_inside_dir(travis_setup_cmd, project_path)
#         # then:
#         result_travis_config = yaml_load(result.project.join(".travis.yml").open())
#         min_size_of_encrypted_password = 50
#         assert len(result_travis_config["deploy"]["password"]["secure"]) > min_size_of_encrypted_password


def test_bake_without_travis_pypi_setup(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_pypi_deployment_with_travis': 'n'}) as result:
        result_travis_config = yaml_load(result.project.join(".travis.yml").open())
        assert "deploy" not in result_travis_config
        assert "python" == result_travis_config["language"]
        found_toplevel_files = [f.basename for f in result.project.listdir()]


def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(cookies, extra_context={'create_thanks_file': 'n'}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'THANKS.md' not in found_toplevel_files
        doc_files = [f.basename for f in result.project.join('docs').listdir()]
        assert 'thanks.rst' not in doc_files

        # Assert there are no spaces in the toc tree
        docs_index_path = result.project.join('docs/index.rst')
        with open(str(docs_index_path)) as index_file:
            assert 'contributing\n   history' in index_file.read()


def test_make_help(cookies):
    with bake_in_temp_dir(cookies) as result:
        output = check_output_inside_dir('make help', str(result.project))
        assert b"check code coverage quickly with the default Python" in output


def test_bake_selecting_license(cookies):
    license_strings = {
        'MIT license': 'MIT ',
        'BSD license': 'Redistributions of source code must retain the above copyright notice, this',
        'ISC license': 'ISC License',
        'Apache Software License 2.0': 'Licensed under the Apache License, Version 2.0',
        'GNU General Public License v3': 'GNU GENERAL PUBLIC LICENSE',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(cookies, extra_context={'open_source_license': license}) as result:
            assert target_string in result.project.join('LICENSE').read()
            assert license in result.project.join('setup.cfg').read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(cookies, extra_context={'open_source_license': 'Not open source'}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'setup.cfg' in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files
        assert 'License' not in result.project.join('README.md').read()


def test_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_pytest': 'y'}) as result:
        assert result.project.isdir()
        test_file_path = result.project.join('tests/test_python_boilerplate.py')
        lines = test_file_path.readlines()
        assert "import pytest" in ''.join(lines)
        # Test the new pytest target
        run_inside_dir('pytest', str(result.project)) == 0


def test_not_using_pytest(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        test_file_path = result.project.join('tests/test_python_boilerplate.py')
        lines = test_file_path.readlines()
        assert "import unittest" in ''.join(lines)
        assert "import pytest" not in ''.join(lines)


# def test_project_with_hyphen_in_module_name(cookies):
#     result = cookies.bake(extra_context={'project_name': 'something-with-a-dash'})
#     assert result.project is not None
#     project_path = str(result.project)
#
#     # when:
#     travis_setup_cmd = ('python travis_pypi_setup.py'
#                         ' --repo ashwinvis/cookiecutter-pypack --password invalidpass')
#     run_inside_dir(travis_setup_cmd, project_path)
#
#     # then:
#     result_travis_config = yaml_load(open(os.path.join(project_path, ".travis.yml")))
#     assert "secure" in result_travis_config["deploy"]["password"],\
#         "missing password config in .travis.yml"


def test_bake_with_no_console_script(cookies):
    context = {'command_line_interface': "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" not in found_project_files

    setup_path = os.path.join(project_path, 'setup.cfg')
    with open(setup_path, 'r') as setup_file:
        assert 'console_scripts' not in setup_file.read()


@pytest.mark.parametrize('lib', ['Click', 'argparse'])
def test_bake_with_console_script_files(cookies, lib):
    context = {'command_line_interface': lib}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files

    setup_path = os.path.join(project_path, 'setup.cfg')
    with open(setup_path, 'r') as setup_file:
        assert 'console_scripts' in setup_file.read()


@pytest.mark.parametrize('lib', ['Click', 'argparse'])
def test_bake_with_console_script_cli(cookies, lib):
    context = {'command_line_interface': lib}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, 'cli.py')
    module_name = '.'.join([project_slug, 'cli'])
    with inside_dir(os.path.join(project_path, "src")):
        if sys.version_info >= (3, 5):
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            cli = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cli)
        else:
            cli = imp.load_source(module_name, module_path)

    if lib == "Click":
        runner = CliRunner()
        noarg_result = runner.invoke(cli.main)
        assert noarg_result.exit_code == 0
        noarg_output = ' '.join(['Replace this message by putting your code into', project_slug])
        assert noarg_output in noarg_result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message' in help_result.output
    elif lib == "argparse":
        for opt, exit_code in zip(
                ('--help', '-V', 'undefined'),
                (0, 0, 2)
        ):
            try:
                cli.main([opt])
            except SystemExit as e:
                assert e.code == exit_code
