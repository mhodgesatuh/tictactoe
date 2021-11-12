#!/usr/bin/env python3
"""Setup script for packaging cliprt.
To build a package for distribution:
    python setup.py sdist
and upload it to the PyPI with:
    python setup.py upload
Install a link for development work:
    pip install -e .
The manifest.in file is used for data files.
https://github.com/mhodgesatuh/cliprty
"""
from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version='0.2.0',
    description='TicTacToe - class exercise',
    packages=find_packages(),
    python_requires=">=3.6, ",
)
