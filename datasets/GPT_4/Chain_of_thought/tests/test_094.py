import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 9)

    def test_single_element_range(self):
        self.assertEqual(sum_range_list([10, 20, 30], 1, 1), 20)

    def test_full_range(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 4), 15)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            sum_range_list([], 0, 1)

    def test_m_equals_n_plus_1(self):
        self.assertEqual(sum_range_list([10, 20, 30], 2, 1), 0)

    def test_m_greater_than_n(self):
        with self.assertRaises(ValueError):
            sum_range_list([10, 20, 30], 3, 1)

    def test_negative_indices(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -3, -1), 12)

    def test_out_of_bounds_indices(self):
        with self.assertRaises(IndexError):
            sum_range_list([10, 20, 30], 1, 5)

    def test_non_integer_elements(self):
        self.assertEqual(sum_range_list([1.5, 2.5, 3.5], 0, 2), 7.5)

    def test_large_list_and_range(self):
        large_list = list(range(1000))
        self.assertEqual(sum_range_list(large_list, 100, 900), sum(range(100, 901)))

