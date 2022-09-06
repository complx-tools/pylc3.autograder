#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_namespace_packages

with open('README.rst') as f:
    readme = f.read()

requirements = [
    "pip==21.0",
    "setuptools",
    "wheel",
    "pylc3.core",
    "unittest2",
    "enum34",
    "six",
]

setup(
    name='pylc3.autograder',
    version='0.1.1',
    description="Autograder and Unit testing framework for LC-3 code written in Python, exports test results in JSON.",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author="Brandon Whitehead",
    author_email='brandon.whitehead@gatech.edu',
    url='https://github.com/complx-tools/pylc3.autograder',
    license="GNU General Public License v3",
    packages=find_namespace_packages(include=['pylc3.*']),
    install_requires=requirements,
)