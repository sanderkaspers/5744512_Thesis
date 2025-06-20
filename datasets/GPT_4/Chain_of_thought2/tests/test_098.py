import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_majority_present(self): self.assertTrue(is_majority([1, 2, 3, 3, 3, 3, 3], 7, 3))

    def test_not_majority(self): self.assertFalse(is_majority([1, 2, 2, 2, 3, 3], 6, 2))

    def test_element_not_present(self): self.assertFalse(is_majority([1, 1, 2, 2, 2], 5, 3))

    def test_all_elements_same(self): self.assertTrue(is_majority([5, 5, 5, 5], 4, 5))

    def test_single_element_array(self): self.assertTrue(is_majority([7], 1, 7))

    def test_two_element_array_not_majority(self): self.assertFalse(is_majority([3, 4], 2, 3))

    def test_majority_at_end(self): self.assertTrue(is_majority([1, 2, 3, 4, 4, 4, 4], 7, 4))

    def test_majority_at_start(self): self.assertTrue(is_majority([2, 2, 2, 2, 3, 4], 6, 2))

    def test_edge_index_boundary(self): self.assertFalse(is_majority([1, 1, 1, 2, 2, 2], 6, 2))

    def test_empty_array(self): self.assertFalse(is_majority([], 0, 1))

