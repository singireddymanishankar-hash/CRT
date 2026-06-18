import unittest
from pascal_utils import pascal_triangle_row, pascal_triangle


class TestPascalTriangleRow(unittest.TestCase):

    def test_row_0(self):
        self.assertEqual(pascal_triangle_row(0), [1])

    def test_row_1(self):
        self.assertEqual(pascal_triangle_row(1), [1, 1])

    def test_row_2(self):
        self.assertEqual(pascal_triangle_row(2), [1, 2, 1])

    def test_row_4(self):
        self.assertEqual(pascal_triangle_row(4), [1, 4, 6, 4, 1])

    def test_row_symmetry(self):
        row = pascal_triangle_row(5)
        self.assertEqual(row, row[::-1])

    def test_row_starts_and_ends_with_1(self):
        row = pascal_triangle_row(6)
        self.assertEqual(row[0], 1)
        self.assertEqual(row[-1], 1)


class TestPascalTriangle(unittest.TestCase):

    def test_five_rows(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]
        self.assertEqual(pascal_triangle(5), expected)

    def test_one_row(self):
        self.assertEqual(pascal_triangle(1), [[1]])

    def test_zero_rows(self):
        self.assertEqual(pascal_triangle(0), [])

    def test_row_count(self):
        self.assertEqual(len(pascal_triangle(7)), 7)

    def test_sum_of_row(self):
        """Sum of row n should be 2^n."""
        triangle = pascal_triangle(8)
        for i, row in enumerate(triangle):
            self.assertEqual(sum(row), 2 ** i)


if __name__ == "__main__":
    unittest.main()
