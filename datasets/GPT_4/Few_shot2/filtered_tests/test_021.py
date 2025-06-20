import unittest
from datasets.GPT_4.Few_shot2.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_is_sublist_true_middle(self): self.assertTrue(is_sublist([1, 2, 3, 4], [2, 3]))

    def test_is_sublist_true_start(self): self.assertTrue(is_sublist([1, 2, 3], [1, 2]))

    def test_is_sublist_true_end(self): self.assertTrue(is_sublist([1, 2, 3], [2, 3]))

    def test_is_sublist_false_non_contiguous(self): self.assertFalse(is_sublist([1, 2, 3], [1, 3]))

    def test_is_sublist_false_not_present(self): self.assertFalse(is_sublist([1, 2, 3], [4, 5]))

    def test_is_sublist_empty_sublist(self): self.assertTrue(is_sublist([1, 2, 3], []))

    def test_is_sublist_full_list(self): self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_is_sublist_both_empty(self): self.assertTrue(is_sublist([], []))

    def test_is_sublist_sublist_longer(self): self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_is_sublist_duplicates(self): self.assertTrue(is_sublist([1, 2, 2, 3], [2, 2]))

