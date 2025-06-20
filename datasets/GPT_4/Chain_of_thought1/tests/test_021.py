import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_middle_sublist(self): self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))

    def test_prefix(self): self.assertTrue(is_sublist([1, 2, 3], [1, 2]))

    def test_suffix(self): self.assertTrue(is_sublist([1, 2, 3], [2, 3]))

    def test_exact_match(self): self.assertTrue(is_sublist([4, 5, 6], [4, 5, 6]))

    def test_empty_sublist(self): self.assertTrue(is_sublist([1, 2, 3], []))

    def test_sublist_too_long(self): self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_no_match(self): self.assertFalse(is_sublist([1, 2, 3], [4, 5]))

    def test_partial_overlap(self): self.assertFalse(is_sublist([1, 2, 3], [2, 4]))

    def test_both_empty(self): self.assertTrue(is_sublist([], []))

    def test_overlapping_sublist(self): self.assertTrue(is_sublist([1, 2, 1, 2, 1], [1, 2, 1]))

