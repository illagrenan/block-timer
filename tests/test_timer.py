# -*- encoding: utf-8 -*-
# ! python3

import time
from unittest import TestCase

from block_timer.timer import Timer


class BasicTestCase(TestCase):
    # noinspection PyMethodMayBeStatic
    def test_basic(self):
        with Timer(title="Some title") as t:
            time.sleep(1 / 3)

        self.assertIsInstance(t, Timer)
        self.assertIsInstance(str(t), str)
        self.assertIsInstance(repr(t), str)
        self.assertIsInstance(float(t), float)
        self.assertGreaterEqual(t.elapsed, 1 / 3)  # a >= b

        self.assertTrue(hasattr(t, 'elapsed'))
        self.assertIsInstance(t.elapsed, float)

        self.assertEqual(float(t), t.elapsed)

    def test_decorator(self):
        @Timer()
        def some_dummy_function():
            return 42

        self.assertTrue(callable(some_dummy_function))
        self.assertEqual(some_dummy_function.__wrapped__.__name__, "some_dummy_function")
        self.assertEqual(42, some_dummy_function())
