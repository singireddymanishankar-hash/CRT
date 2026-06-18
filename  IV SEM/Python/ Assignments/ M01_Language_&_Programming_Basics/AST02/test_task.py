'''
'''
import unittest
from task import even_odd

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(even_odd(3), "Weird")

    def test_multiple_digits(self):
        self.assertEqual(even_odd(24), "Not Weird")

    def test_with_zero(self):
        self.assertEqual(even_odd(10), "Weird")

    def test_even_2_to_5(self):
        self.assertEqual(even_odd(4), "Not Weird")

    def test_even_2(self):
        self.assertEqual(even_odd(2), "Not Weird")

    def test_odd_large(self):
        self.assertEqual(even_odd(21), "Weird")

    def test_odd_small(self):
        self.assertEqual(even_odd(1), "Weird")

    def test_even_6_to_20(self):
        self.assertEqual(even_odd(6), "Weird")

    def test_even_20(self):
        self.assertEqual(even_odd(20), "Weird")

    def test_even_above_20(self):
        self.assertEqual(even_odd(22), "Not Weird")

if __name__ == "__main__":
    unittest.main()
