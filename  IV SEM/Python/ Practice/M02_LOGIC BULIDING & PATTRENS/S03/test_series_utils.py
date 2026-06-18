import unittest
from series_utils import (
    arithmetic_series,
    geometric_series,
    fibonacci_series,
    factorial_series,
    is_palindrome,
)


class TestArithmeticSeries(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(arithmetic_series(1, 2, 5), [1, 3, 5, 7, 9])

    def test_zero_diff(self):
        self.assertEqual(arithmetic_series(5, 0, 3), [5, 5, 5])

    def test_negative_diff(self):
        self.assertEqual(arithmetic_series(10, -3, 4), [10, 7, 4, 1])

    def test_single_term(self):
        self.assertEqual(arithmetic_series(7, 5, 1), [7])


class TestGeometricSeries(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(geometric_series(2, 3, 4), [2, 6, 18, 54])

    def test_ratio_one(self):
        self.assertEqual(geometric_series(5, 1, 3), [5, 5, 5])

    def test_ratio_two(self):
        self.assertEqual(geometric_series(1, 2, 5), [1, 2, 4, 8, 16])

    def test_single_term(self):
        self.assertEqual(geometric_series(3, 10, 1), [3])


class TestFibonacciSeries(unittest.TestCase):

    def test_first_five(self):
        self.assertEqual(fibonacci_series(5), [0, 1, 1, 2, 3])

    def test_first_eight(self):
        self.assertEqual(fibonacci_series(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_one_term(self):
        self.assertEqual(fibonacci_series(1), [0])

    def test_zero_terms(self):
        self.assertEqual(fibonacci_series(0), [])

    def test_two_terms(self):
        self.assertEqual(fibonacci_series(2), [0, 1])


class TestFactorialSeries(unittest.TestCase):

    def test_first_five(self):
        self.assertEqual(factorial_series(5), [1, 2, 6, 24, 120])

    def test_one(self):
        self.assertEqual(factorial_series(1), [1])

    def test_zero(self):
        self.assertEqual(factorial_series(0), [])

    def test_three(self):
        self.assertEqual(factorial_series(3), [1, 2, 6])


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_single_char(self):
        self.assertTrue(is_palindrome("a"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome("abba"))

    def test_numeric_string(self):
        self.assertTrue(is_palindrome("12321"))

    def test_not_palindrome_number(self):
        self.assertFalse(is_palindrome("12345"))


if __name__ == "__main__":
    unittest.main()
