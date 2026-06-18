import unittest
from task import Reverse_String

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(Reverse_String("hello"), "olleh")

    def test_multiple_digits(self):
        self.assertEqual(Reverse_String("world"), "dlrow")

    def test_with_zero(self):
        self.assertEqual(Reverse_String("python"), "nohtyp")

    def test_empty_string(self):
        self.assertEqual(Reverse_String(""), "")

    def test_single_char(self):
        self.assertEqual(Reverse_String("a"), "a")

    def test_palindrome(self):
        self.assertEqual(Reverse_String("racecar"), "racecar")

    def test_with_spaces(self):
        self.assertEqual(Reverse_String("ab cd"), "dc ba")

    def test_with_numbers(self):
        self.assertEqual(Reverse_String("abc123"), "321cba")

if __name__ == "__main__":
    unittest.main()
