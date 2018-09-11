# -*- encoding: utf-8 -*-
# ! python3

import io
import re
import time
from contextlib import redirect_stdout
from unittest import TestCase

from block_timer.timer import Timer


class BasicTestCase(TestCase):
    def test_basic(self):
        with Timer(title="Some title") as t:
            time.sleep(1 / 3)

        self.assertIsInstance(t, Timer)
        self.assertIsInstance(str(t), str)
        self.assertIsInstance(repr(t), str)
        self.assertIsInstance(float(t), float)
        self.assertGreaterEqual(t.elapsed, 1 / 4)  # a >= b

        self.assertTrue(hasattr(t, 'elapsed'))
        self.assertIsInstance(t.elapsed, float)

        self.assertEqual(float(t), t.elapsed)

    def test_elapsed(self):
        t = Timer()

        self.assertEqual(0, t.elapsed)

        t.__enter__()
        time.sleep(1 / 7)
        t.__exit__()

        self.assertGreater(t.elapsed, 0)  # a > b

    def test_multiple_instances(self):
        with Timer(title="Some title") as t1:
            time.sleep(1 / 5)

        with Timer(title="Some title") as t2:
            time.sleep(1 / 5)

        self.assertIsNot(t1, t2)

    def test_stdout(self):
        with io.StringIO() as buffer1:
            with Timer(title="Some title", print_file=buffer1):
                time.sleep(1 / 5)

            output1 = buffer1.getvalue()

        self.assertRegex(output1, re.compile(r"\[Some title\] Total time \d+\.\d+ seconds.\n", re.UNICODE))

        with io.StringIO() as buffer2:
            with Timer(title="Different title", print_file=buffer2):
                time.sleep(1 / 5)

            output2 = buffer2.getvalue()

        self.assertRegex(output2, re.compile(r"\[Different title\] Total time \d+\.\d+ seconds.\n", re.UNICODE))

    def test_decorator(self):
        @Timer()
        def some_dummy_function():
            return 42

        self.assertTrue(callable(some_dummy_function))
        self.assertEqual(some_dummy_function.__wrapped__.__name__, "some_dummy_function")
        self.assertEqual(42, some_dummy_function())
