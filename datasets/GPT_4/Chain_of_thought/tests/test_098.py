import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_majority([1, 1, 1, 2, 3], 5, 1))

    def test_no_majority(self):
        self.assertFalse(is_majority([1, 1, 2, 2, 3, 3], 6, 2))

    def test_x_not_in_array(self):
        self.assertFalse(is_majority([1, 2, 3, 4, 5], 5, 6))

    def test_all_elements_are_x(self):
        self.assertTrue(is_majority([2, 2, 2, 2, 2], 5, 2))

    def test_single_element_array(self):
        self.assertTrue(is_majority([3], 1, 3))

    def test_size_n_over_2_plus_1(self):
        self.assertTrue(is_majority([2, 2, 2, 3, 3], 5, 2))

    def test_size_n_over_2(self):
        self.assertFalse(is_majority([2, 2, 3, 3], 4, 2))

    def test_edge_case_small_n(self):
        self.assertTrue(is_majority([1, 1], 2, 1))

    def test_mixed_elements(self):
        self.assertFalse(is_majority([1, 2, 3, 4, 5], 5, 3))

    def test_non_x_duplicates(self):
        self.assertFalse(is_majority([1, 1, 2, 2, 2, 3], 6, 2))

