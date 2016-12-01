=======================================================
Block Timer: Measure execution time of your code blocks
=======================================================

.. image:: https://badge.fury.io/py/block-timer.svg
        :target: https://pypi.python.org/pypi/block-timer
        :alt: PyPi

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://pypi.python.org/pypi/block-timer/
        :alt: MIT

.. image:: https://api.travis-ci.org/illagrenan/block-timer.svg
        :target: https://travis-ci.org/illagrenan/block-timer
        :alt: TravisCI

.. image:: https://coveralls.io/repos/github/illagrenan/block-timer/badge.svg?branch=master
        :target: https://coveralls.io/github/illagrenan/block-timer?branch=master
        :alt: Coverage

.. image:: https://pyup.io/repos/github/illagrenan/block-timer/shield.svg
     :target: https://pyup.io/repos/github/illagrenan/block-timer/
     :alt: Updates

.. image:: https://pyup.io/repos/github/illagrenan/block-timer/python-3-shield.svg
     :target: https://pyup.io/repos/github/illagrenan/block-timer/
     :alt: Python 3

Introduction
------------

You can easily measure blocks of code using ``Timer`` class as context manager or as method/function decorator:

.. code:: python

    from block_timer.timer import Timer

    with Timer() as t:
        pass # Some long running operation

    # Total time ... seconds will be printed
    # or you can use elapsed property:
    print(t.elapsed)

Installation
------------

- Supported Python versions are: **only** ``3.5``.

.. code:: shell

    pip install --upgrade block-timer


Resources
---------

- `time.perf_counter() on Python Doc <https://docs.python.org/3/library/time.html#time.perf_counter>`_


License
-------

The MIT License (MIT)

Copyright (c) 2016 Vašek Dohnal (@illagrenan)

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
