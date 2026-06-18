import unittest
from pattern_utils import (
    square_star_pattern,
    right_angle_triangle,
    reverse_right_angle_triangle,
    pyramid_pattern,
)


class TestSquareStarPattern(unittest.TestCase):

    def test_size_3(self):
        result = square_star_pattern(3)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "* * * ")

    def test_size_1(self):
        self.assertEqual(square_star_pattern(1), ["* "])

    def test_all_rows_equal(self):
        result = square_star_pattern(4)
        self.assertTrue(all(row == result[0] for row in result))


class TestRightAngleTriangle(unittest.TestCase):

    def test_size_3(self):
        result = right_angle_triangle(3)
        self.assertEqual(result, ["* ", "* * ", "* * * "])

    def test_size_1(self):
        self.assertEqual(right_angle_triangle(1), ["* "])

    def test_row_count(self):
        self.assertEqual(len(right_angle_triangle(5)), 5)

    def test_last_row_has_n_stars(self):
        n = 4
        result = right_angle_triangle(n)
        self.assertEqual(result[-1].count("*"), n)


class TestReverseRightAngleTriangle(unittest.TestCase):

    def test_size_3(self):
        result = reverse_right_angle_triangle(3)
        self.assertEqual(result, ["***", "**", "*"])

    def test_size_1(self):
        self.assertEqual(reverse_right_angle_triangle(1), ["*"])

    def test_first_row_has_n_stars(self):
        n = 5
        result = reverse_right_angle_triangle(n)
        self.assertEqual(result[0].count("*"), n)


class TestPyramidPattern(unittest.TestCase):

    def test_size_3(self):
        result = pyramid_pattern(3)
        self.assertEqual(result[0], "  *")
        self.assertEqual(result[1], " ***")
        self.assertEqual(result[2], "*****")

    def test_size_1(self):
        self.assertEqual(pyramid_pattern(1), ["*"])

    def test_row_count(self):
        self.assertEqual(len(pyramid_pattern(4)), 4)

    def test_last_row_width(self):
        n = 5
        result = pyramid_pattern(n)
        self.assertEqual(len(result[-1]), 2 * n - 1)


if __name__ == "__main__":
    unittest.main()
