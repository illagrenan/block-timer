# -*- encoding: utf-8 -*-
# ! python3

import sys
import time
from contextlib import ContextDecorator
from typing import Optional

__all__ = ["Timer"]


class Timer(ContextDecorator):
    """
    Timer class that can be used both as a context manager and function/method decorator.

    Usage:

    >>> import math
    >>> import time
    >>>
    >>> with Timer():
    ...    for i in range(42):
    ...        print("{}! = {:.5}...".format(i**2, str(math.factorial(i**2))))
    >>>
    >>> @Timer(title="Second")
    ... def some_func():
    ...     time.sleep(1)
    >>>
    >>> with Timer(title="Some title") as t:
    ...    for i in range(42):
    ...        print("{}! = {:.5}...".format(i**2, str(math.factorial(i**2))))
    >>>
    >>> print(t.elapsed)
    """

    def __init__(self, title: str = "", print_title: Optional[bool] = True, print_file=sys.stdout):
        """
        Instantiate new Timer.

        :param title: Title (prefix) that will be printed
        :param print_title: Should print elapsed time?
        :param print_file: File that will be passed to print function, see: https://docs.python.org/3/library/functions.html#print
        """
        self._title = title
        self._print_title = print_title
        self._print_file = print_file
        self._elapsed = 0

    def __float__(self) -> float:
        return float(self.elapsed)

    def __str__(self) -> str:
        """
        “informal” or nicely printable string representation of an object
        """
        return "Elapsed {}".format(self.__repr__())

    def __repr__(self) -> str:
        """
        “official” string representation of an object.
        """
        return str(float(self))

    def __enter__(self) -> 'Timer':
        self.start = time.perf_counter()

        return self

    def __exit__(self, *args):
        self._elapsed = time.perf_counter() - self.start

        if self._print_title:
            title = "[{}] ".format(self._title) if self._title else ""
            formatted_title = '{title}Total time {total_seconds:.5f} seconds.'.format(title=title, total_seconds=self._elapsed)
            print(formatted_title, file=self._print_file)

    @property
    def elapsed(self) -> float:
        return self._elapsed
