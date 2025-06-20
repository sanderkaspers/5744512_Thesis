import unittest
from datasets.GPT_4.Few_shot1.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_is_sublist_true_middle(self): self.assertEqual(is_sublist([1, 2, 3, 4], [2, 3]), True)

    def test_is_sublist_true_start(self): self.assertEqual(is_sublist([1, 2, 3], [1, 2]), True)

    def test_is_sublist_true_end(self): self.assertEqual(is_sublist([1, 2, 3], [2, 3]), True)

    def test_is_sublist_whole_list(self): self.assertEqual(is_sublist([1, 2, 3], [1, 2, 3]), True)

    def test_is_sublist_empty_sublist(self): self.assertEqual(is_sublist([1, 2, 3], []), True)

    def test_is_sublist_empty_main_list(self): self.assertEqual(is_sublist([], [1]), False)

    def test_is_sublist_both_empty(self): self.assertEqual(is_sublist([], []), True)

    def test_is_sublist_not_present(self): self.assertEqual(is_sublist([1, 2, 3], [4, 5]), False)

    def test_is_sublist_same_elements_different_order(self): self.assertEqual(is_sublist([1, 2, 3], [3, 2]), False)

    def test_is_sublist_sublist_larger(self): self.assertEqual(is_sublist([1, 2], [1, 2, 3]), False)

