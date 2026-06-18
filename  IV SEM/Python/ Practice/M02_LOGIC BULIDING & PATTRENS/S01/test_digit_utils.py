import unittest
from digit_utils import count_digits, sum_of_digits, reverse_number, is_palindrome_number


class TestCountDigits(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(count_digits(5), 1)

    def test_two_digits(self):
        self.assertEqual(count_digits(42), 2)

    def test_large_number(self):
        self.assertEqual(count_digits(12345), 5)

    def test_zero(self):
        self.assertEqual(count_digits(0), 1)

    def test_negative(self):
        self.assertEqual(count_digits(-123), 3)


class TestSumOfDigits(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(sum_of_digits(7), 7)

    def test_multi_digit(self):
        self.assertEqual(sum_of_digits(123), 6)

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0)

    def test_all_nines(self):
        self.assertEqual(sum_of_digits(999), 27)

    def test_negative(self):
        self.assertEqual(sum_of_digits(-45), 9)


class TestReverseNumber(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(reverse_number(123), 321)

    def test_single_digit(self):
        self.assertEqual(reverse_number(5), 5)

    def test_trailing_zeros(self):
        self.assertEqual(reverse_number(1200), 21)

    def test_zero(self):
        self.assertEqual(reverse_number(0), 0)

    def test_palindrome(self):
        self.assertEqual(reverse_number(12321), 12321)


class TestIsPalindromeNumber(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome_number(121))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome_number(123))

    def test_single_digit(self):
        self.assertTrue(is_palindrome_number(7))

    def test_zero(self):
        self.assertTrue(is_palindrome_number(0))

    def test_large_palindrome(self):
        self.assertTrue(is_palindrome_number(12321))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome_number(1221))


if __name__ == "__main__":
    unittest.main()
