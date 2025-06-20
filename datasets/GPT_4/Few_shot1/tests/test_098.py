import unittest
from datasets.GPT_4.Few_shot1.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_is_majority_true_simple(self): self.assertTrue(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))

    def test_is_majority_false_simple(self): self.assertFalse(is_majority([1, 2, 3, 3, 3, 10], 6, 3))

    def test_is_majority_not_present(self): self.assertFalse(is_majority([1, 2, 4, 5], 4, 3))

    def test_is_majority_all_elements(self): self.assertTrue(is_majority([3, 3, 3, 3, 3], 5, 3))

    def test_is_majority_first_half(self): self.assertFalse(is_majority([2, 2, 2, 3, 4, 5], 6, 2))

    def test_is_majority_last_half(self): self.assertFalse(is_majority([1, 2, 3, 4, 5, 5, 5], 7, 5))

    def test_is_majority_edge_case_middle(self): self.assertFalse(is_majority([1, 1, 2, 2, 2], 5, 2))

    def test_is_majority_exact_half(self): self.assertFalse(is_majority([1, 2, 2, 2, 3, 4], 6, 2))

    def test_is_majority_above_half(self): self.assertTrue(is_majority([1, 2, 2, 2, 2, 3], 6, 2))

    def test_is_majority_first_element(self): self.assertFalse(is_majority([1, 1, 2, 3, 4], 5, 1))

    def test_is_majority_last_element(self): self.assertFalse(is_majority([1, 2, 3, 4, 5, 5], 6, 5))

    def test_is_majority_single_element_true(self): self.assertTrue(is_majority([3], 1, 3))

    def test_is_majority_single_element_false(self): self.assertFalse(is_majority([3], 1, 2))

    def test_is_majority_two_elements_true(self): self.assertTrue(is_majority([3, 3], 2, 3))

    def test_is_majority_two_elements_false(self): self.assertFalse(is_majority([2, 3], 2, 3))

    def test_is_majority_all_same(self): self.assertTrue(is_majority([5]*10, 10, 5))

    def test_is_majority_half_plus_one(self): self.assertTrue(is_majority([2]*6 + [3]*5, 11, 2))

    def test_is_majority_half(self): self.assertFalse(is_majority([2]*5 + [3]*5, 10, 2))

    def test_is_majority_unsorted_input(self): self.assertFalse(is_majority([3, 1, 2, 3, 3], 5, 3))

