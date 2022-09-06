================
pylc3.autograder
================

Autograder framework for LC-3, based off liblc3 and pylc3.core

Exports test results in JSON. JSON output format is configurable.
Note that this doesn't export a grade in the JSON. A user script can then easily parse the
JSON and then assign points per each assertion passed.

For autograder examples see https://github.com/complx-tools/pylc3.autograder.examples

* Free software: GNU General Public License v3
* Documentation: https://pylc3.autograder.readthedocs.io.

Installation
------------

* Install python, boost-python (should be compiled with your version of Python) and castxml.

``$ sudo add-apt-repository ppa:tricksterguy87/complx``
``$ sudo apt update``
``$ sudo apt-get install -y build-essential cmake libboost-python-dev castxml python-pip liblc3-dev``

It is suggested to also install liblc3-plugins.

* Install scikit-build and dependencies for pylc3.core

``$ sudo pip install scikit-build pygccxml pyplusplus``

* Install this package from PyPI:

``$ sudo pip install pylc3.autograder``

* Import it in Python:

``import pylc3.autograder``