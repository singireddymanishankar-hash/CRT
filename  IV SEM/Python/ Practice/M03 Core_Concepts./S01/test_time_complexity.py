import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from importlib import import_module

# Import the fibo function directly to avoid running the __main__ block
import importlib.util
spec = importlib.util.spec_from_file_location(
    "time_complexity",
    os.path.join(os.path.dirname(__file__), "PS01_Time complexity.py")
)
mod = importlib.util.module_from_spec(spec)
mod.__name__ = "time_complexity"
# Patch input/print to prevent __main__ side effects
import builtins
_orig_input = builtins.input
builtins.input = lambda *a, **kw: "0"
spec.loader.exec_module(mod)
builtins.input = _orig_input

fibo = mod.fibo


class TestFibo(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibo(0), 0)

    def test_one(self):
        self.assertEqual(fibo(1), 1)

    def test_two(self):
        self.assertEqual(fibo(2), 1)

    def test_five(self):
        self.assertEqual(fibo(5), 5)

    def test_ten(self):
        self.assertEqual(fibo(10), 55)

    def test_negative(self):
        self.assertEqual(fibo(-1), 0)

    def test_seven(self):
        self.assertEqual(fibo(7), 13)

    def test_sequence_property(self):
        """fibo(n) = fibo(n-1) + fibo(n-2) for n >= 2"""
        for n in range(2, 12):
            self.assertEqual(fibo(n), fibo(n - 1) + fibo(n - 2))


if __name__ == "__main__":
    unittest.main()
