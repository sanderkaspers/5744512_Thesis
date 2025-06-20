import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_majority_center(self): self.assertTrue(is_majority([1, 1, 1, 2, 3], 5, 1))

    def test_majority_end(self): self.assertTrue(is_majority([1, 2, 2, 2, 2], 5, 2))

    def test_majority_start(self): self.assertTrue(is_majority([3, 3, 3, 4, 5], 5, 3))

    def test_not_majority(self): self.assertFalse(is_majority([1, 2, 2, 3, 4], 5, 2))

    def test_not_present(self): self.assertFalse(is_majority([1, 2, 3, 4, 5], 5, 6))

    def test_single_element(self): self.assertTrue(is_majority([1], 1, 1))

    def test_two_same(self): self.assertTrue(is_majority([2, 2], 2, 2))

    def test_two_diff(self): self.assertFalse(is_majority([1, 2], 2, 1))

    def test_all_same(self): self.assertTrue(is_majority([7]*10, 10, 7))

    def test_empty_array(self): self.assertFalse(is_majority([], 0, 1))

    def test_first_occurrence_late(self): self.assertTrue(is_majority([1, 1, 2, 2, 2], 5, 2))

    def test_type_mismatch(self): self.assertFalse(is_majority([2, 2, 2], 3, '2'))

    def test_just_under_majority(self): self.assertFalse(is_majority([1]*4999 + [2]*5001, 10000, 1))

    def test_just_meets_majority(self): self.assertTrue(is_majority([1]*5001 + [2]*4999, 10000, 1))

