import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_consistent_mapping(self): self.assertTrue(is_samepatterns(['a', 'b', 'a'], [1, 2, 1]))

    def test_many_to_one(self): self.assertTrue(is_samepatterns(['x', 'y', 'z'], [1, 1, 1]))

    def test_all_same_key(self): self.assertTrue(is_samepatterns(['c', 'c', 'c'], [2, 2, 2]))

    def test_conflicting_mapping(self): self.assertFalse(is_samepatterns(['a', 'b', 'a'], [1, 2, 3]))

    def test_unequal_length(self): self.assertFalse(is_samepatterns(['a', 'b'], [1]))

    def test_both_empty(self): self.assertTrue(is_samepatterns([], []))

    def test_one_empty(self): self.assertFalse(is_samepatterns([], [1]))

    def test_single_element(self): self.assertTrue(is_samepatterns(['x'], [42]))

    def test_shared_value(self): self.assertTrue(is_samepatterns(['a', 'b'], [1, 1]))

    def test_mixed_types(self): self.assertTrue(is_samepatterns(['x', 1], ['a', 'b']))

    def test_duplicate_values_ok(self): self.assertTrue(is_samepatterns(['m', 'n', 'm', 'n'], [2, 3, 2, 3]))

