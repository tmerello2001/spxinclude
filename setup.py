#!/bin/python3
# coding: utf-8
"""setup file."""

from os import path
from setuptools import find_packages, setup

from spxinclude import __version__


here = path.abspath(path.dirname(__file__))

# Get requirements from the requirements.txt file
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as req_f:
    requirements = req_f.read().splitlines()

# Get the long description from the README.md file
with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='spxinclude',
    version=__version__,
    license='MIT',
    author='Tomas Merello',
    author_email='tomas@merello.net',
    description='Sphinx include methods',
    long_description=long_description,
    url='https://github.com/tmerello2001/spxinclude.git',
    keywords=['Sphinx', 'include', 'directives', 'Github', 'Git', 'remote'],
    packages=find_packages(include=['spxinclude', 'spxinclude.*']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
