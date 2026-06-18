import unittest
from collections_utils import (
    create_list,
    access_first,
    access_last,
    repeat_list,
    remove_element,
    slice_list,
)


class TestCreateList(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(create_list(1, 2, 3), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(create_list(), [])

    def test_single(self):
        self.assertEqual(create_list(42), [42])

    def test_mixed_types(self):
        self.assertEqual(create_list(1, "a", 3.0), [1, "a", 3.0])


class TestAccessFirst(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(access_first([10, 20, 30]), 10)

    def test_single_element(self):
        self.assertEqual(access_first([99]), 99)

    def test_empty_raises(self):
        with self.assertRaises(IndexError):
            access_first([])


class TestAccessLast(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(access_last([10, 20, 30]), 30)

    def test_single_element(self):
        self.assertEqual(access_last([99]), 99)

    def test_empty_raises(self):
        with self.assertRaises(IndexError):
            access_last([])


class TestRepeatList(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(repeat_list([1, 2], 3), [1, 2, 1, 2, 1, 2])

    def test_zero_times(self):
        self.assertEqual(repeat_list([1, 2], 0), [])

    def test_one_time(self):
        self.assertEqual(repeat_list([1, 2, 3], 1), [1, 2, 3])


class TestRemoveElement(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(remove_element([1, 2, 3, 4, 5], 3), [1, 2, 4, 5])

    def test_first_occurrence_only(self):
        self.assertEqual(remove_element([1, 2, 3, 2], 2), [1, 3, 2])

    def test_not_found_raises(self):
        with self.assertRaises(ValueError):
            remove_element([1, 2, 3], 99)

    def test_does_not_modify_original(self):
        original = [1, 2, 3]
        remove_element(original, 2)
        self.assertEqual(original, [1, 2, 3])


class TestSliceList(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(slice_list([1, 2, 3, 4, 5], 1, 4), [2, 3, 4])

    def test_full_slice(self):
        self.assertEqual(slice_list([1, 2, 3], 0, 3), [1, 2, 3])

    def test_empty_slice(self):
        self.assertEqual(slice_list([1, 2, 3], 1, 1), [])

    def test_out_of_bounds(self):
        self.assertEqual(slice_list([1, 2], 0, 10), [1, 2])


if __name__ == "__main__":
    unittest.main()
