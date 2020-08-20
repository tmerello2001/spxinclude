#!/bin/python3
# coding: utf-8
"""setup file."""

from os import path

from setuptools import find_packages, setup

from spxinclude import __version__


here = path.abspath(path.dirname(__file__))

setup(
    name='spxinclude',
    version=__version__,
    description='Sphinx include methods',
    packages=find_packages(include=['spxinclude']),
    install_requires=['GitPython==3.1.7', 'Sphinx==3.2.1'],
)
