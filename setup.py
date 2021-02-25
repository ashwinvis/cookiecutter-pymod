# !/usr/bin/env python
from pathlib import Path
from setuptools import setup


here = Path(__file__).parent
requirements = (here / "dev-requirements.txt").read_text().splitlines()

setup(
    use_scm_version=True,
    install_requires=requirements,
)
