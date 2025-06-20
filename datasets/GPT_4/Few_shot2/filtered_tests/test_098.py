import unittest
from datasets.GPT_4.Few_shot2.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_is_majority_true_middle(self): self.assertTrue(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))

    def test_is_majority_false_middle(self): self.assertFalse(is_majority([1, 2, 3, 3, 3, 10], 6, 3))

    def test_is_majority_at_start(self): self.assertTrue(is_majority([2, 2, 2, 2, 3, 4], 6, 2))

    def test_is_majority_not_present(self): self.assertFalse(is_majority([1, 2, 4, 5, 6], 5, 3))

    def test_is_majority_single_element_true(self): self.assertTrue(is_majority([5], 1, 5))

    def test_is_majority_single_element_false(self): self.assertFalse(is_majority([5], 1, 3))

    def test_is_majority_even_length_true(self): self.assertTrue(is_majority([2, 2, 2, 3], 4, 2))

    def test_is_majority_even_length_false(self): self.assertFalse(is_majority([2, 2, 3, 3], 4, 2))

    def test_is_majority_just_half_not_majority(self): self.assertFalse(is_majority([3, 3, 4, 4], 4, 3))

