import unittest
from datasets.GPT_4.Few_shot2.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_is_samepatterns_matching_pattern(self): self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['a', 'b', 'a']))

    def test_is_samepatterns_non_matching_pattern(self): self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['a', 'a', 'b']))

    def test_is_samepatterns_different_lengths(self): self.assertFalse(is_samepatterns(['red', 'blue'], ['a', 'b', 'c']))

    def test_is_samepatterns_all_unique(self): self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['x', 'y', 'z']))

    def test_is_samepatterns_all_same(self): self.assertTrue(is_samepatterns(['red', 'red', 'red'], ['x', 'x', 'x']))

    def test_is_samepatterns_single_element(self): self.assertTrue(is_samepatterns(['red'], ['a']))

    def test_is_samepatterns_empty_lists(self): self.assertTrue(is_samepatterns([], []))

    def test_is_samepatterns_duplicate_to_unique(self): self.assertFalse(is_samepatterns(['red', 'red'], ['x', 'y']))

    def test_is_samepatterns_unique_to_duplicate(self): self.assertFalse(is_samepatterns(['red', 'blue'], ['x', 'x']))

