import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_typical_case_with_duplicates(self):
        self.assertTrue(test_duplicate([1, 2, 3, 2]))

    def test_no_duplicates(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4]))

    def test_empty_array(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_all_duplicates(self):
        self.assertTrue(test_duplicate([2, 2, 2, 2]))

    def test_large_array_with_duplicates(self):
        self.assertTrue(test_duplicate(list(range(10000)) + [9999]))

    def test_array_with_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -3, -1]))

    def test_mixed_positive_and_negative_numbers(self):
        self.assertTrue(test_duplicate([1, -1, 2, -2, 1]))

    def test_array_with_zero(self):
        self.assertFalse(test_duplicate([0, 1, 2, 3]))

    def test_array_with_max_min_integers(self):
        self.assertFalse(test_duplicate([2147483647, -2147483648]))

    def test_repeated_pattern(self):
        self.assertTrue(test_duplicate([1, 2, 3, 1, 2, 3]))

    def test_non_consecutive_duplicates(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 2]))

    def test_array_with_floating_point_numbers(self):
        self.assertTrue(test_duplicate([1.1, 2.2, 3.3, 2.2]))

    def test_mixed_data_types(self):
        self.assertTrue(test_duplicate([1, '1', 2, 2]))

