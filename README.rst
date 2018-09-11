=======================================================
Block Timer: Measure execution time of your code blocks
=======================================================

.. image:: https://img.shields.io/pypi/v/block-timer.svg
        :target: https://pypi.python.org/pypi/block-timer
        :alt: PyPi

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://pypi.python.org/pypi/block-timer/
        :alt: MIT

.. image:: https://img.shields.io/travis/illagrenan/block-timer.svg
        :target: https://travis-ci.org/illagrenan/block-timer
        :alt: TravisCI

.. image:: https://img.shields.io/coveralls/illagrenan/block-timer.svg
        :target: https://coveralls.io/github/illagrenan/block-timer?branch=master
        :alt: Coverage

.. image:: https://pyup.io/repos/github/illagrenan/block-timer/shield.svg
     :target: https://pyup.io/repos/github/illagrenan/block-timer/
     :alt: Updates

.. image:: https://img.shields.io/pypi/implementation/block-timer.svg
	:target: https://pypi.python.org/pypi/block-timer/
	:alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/pyversions/block-timer.svg
	:target: https://pypi.python.org/pypi/block-timer/
	:alt: Supported Python versions

Installation
------------

- Supported Python versions are: ``3.4``, ``3.5``, ``3.6`` and ``3.7``.

.. code:: shell

    pip install --upgrade block-timer

Usage
-----

You can easily measure blocks of code using ``Timer`` class as context manager or as method/function decorator with Block Timer:

Elapsed time will be printed using standard ``print`` function:

.. code:: python

    from block_timer.timer import Timer

    with Timer():
        pass # Some operation

    # Total time ... seconds will be printed

If you have multiple blocks of code, you can set ``title`` attribute:

.. code:: python

    from block_timer.timer import Timer

    with Timer(title="Block A"):
        pass # Some operation

    # [Block A] Total time ... seconds will be printed

    with Timer(title="Block B"):
        pass # Some operation

    # [Block B] Total time ... seconds will be printed

Elapsed time (in fractional seconds) can be accessed by ``elapsed`` property. You can also disable printing by ``print_title=False``:

.. code:: python

    from block_timer.timer import Timer

    with Timer(print_title=False) as t:
        pass # Some operation

    print("Elapsed time: {:f} seconds".format(t.elapsed))


You can redirect output for print function:

.. code:: python

    import sys

    from block_timer.timer import Timer

    with Timer(print_file=sys.stdout):
        pass # Some operation

``Timer`` class can be used as a method/function decorator:

.. code:: python

    @Timer(title="Foo")
    def some_func():
        time.sleep(1)

    some_func()
    # [Foo] Total time ... seconds will be printed

Resources
---------

- `time.perf_counter() on Python Doc <https://docs.python.org/3/library/time.html#time.perf_counter>`_


License
-------

The MIT License (MIT)
