# pylc3.autograder

[![pypi](https://img.shields.io/pypi/v/pylc3.autograder.svg)](https://pypi.python.org/pypi/pylc3.autograder)

Autograder and Unit testing framework for LC-3 code written in Python, exports test results in JSON. 

JSON output format is configurable. 

**Note** that this package doesn't export any grades. The intended use is just exporting the test results in JSON afterwards a script can then easily parse the JSON and assign points per each assertion passed.

For examples see [pylc3.autograder.examples](https://github.com/complx-tools/pylc3.autograder.examples)
