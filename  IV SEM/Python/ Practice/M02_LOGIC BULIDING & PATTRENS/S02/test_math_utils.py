import unittest
from math_utils import get_factors, count_factors, is_prime, primes_in_range, factorial


class TestGetFactors(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(get_factors(7), [1, 7])

    def test_composite_number(self):
        self.assertEqual(get_factors(12), [1, 2, 3, 4, 6, 12])

    def test_one(self):
        self.assertEqual(get_factors(1), [1])

    def test_perfect_square(self):
        self.assertEqual(get_factors(16), [1, 2, 4, 8, 16])

    def test_small(self):
        self.assertEqual(get_factors(6), [1, 2, 3, 6])


class TestCountFactors(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(count_factors(7), 2)

    def test_composite(self):
        self.assertEqual(count_factors(12), 6)

    def test_one(self):
        self.assertEqual(count_factors(1), 1)


class TestIsPrime(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(7))

    def test_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_negative(self):
        self.assertFalse(is_prime(-5))

    def test_large_prime(self):
        self.assertTrue(is_prime(97))

    def test_large_composite(self):
        self.assertFalse(is_prime(100))


class TestPrimesInRange(unittest.TestCase):

    def test_small_range(self):
        self.assertEqual(primes_in_range(1, 10), [2, 3, 5, 7])

    def test_range_with_no_primes(self):
        self.assertEqual(primes_in_range(24, 28), [])

    def test_single_prime(self):
        self.assertEqual(primes_in_range(7, 7), [7])

    def test_range_20_to_30(self):
        self.assertEqual(primes_in_range(20, 30), [23, 29])


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_five(self):
        self.assertEqual(factorial(5), 120)

    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)

    def test_three(self):
        self.assertEqual(factorial(3), 6)


if __name__ == "__main__":
    unittest.main()
