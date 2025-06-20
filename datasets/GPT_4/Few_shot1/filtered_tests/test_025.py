import unittest
from datasets.GPT_4.Few_shot1.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_samepatterns_matching_patterns(self): self.assertEqual(is_samepatterns(['red', 'red', 'blue'], ['a', 'a', 'b']), True)

    def test_samepatterns_non_matching_patterns(self): self.assertEqual(is_samepatterns(['red', 'blue', 'blue'], ['a', 'a', 'b']), False)

    def test_samepatterns_different_lengths(self): self.assertEqual(is_samepatterns(['red', 'blue'], ['a']), False)

    def test_samepatterns_all_unique(self): self.assertEqual(is_samepatterns(['red', 'green', 'blue'], ['a', 'b', 'c']), True)

    def test_samepatterns_all_same(self): self.assertEqual(is_samepatterns(['red', 'red', 'red'], ['a', 'a', 'a']), True)

    def test_samepatterns_unique_mismatch(self): self.assertEqual(is_samepatterns(['red', 'green', 'green'], ['a', 'b', 'c']), False)

    def test_samepatterns_empty_lists(self): self.assertEqual(is_samepatterns([], []), True)

    def test_samepatterns_numeric(self): self.assertEqual(is_samepatterns([1, 1, 2], [3, 3, 4]), True)

    def test_samepatterns_mixed_types(self): self.assertEqual(is_samepatterns(['x', 'y'], [1, 1]), False)

    def test_samepatterns_tuple_keys(self): self.assertEqual(is_samepatterns([(1,2), (1,2)], ['a', 'a']), True)

