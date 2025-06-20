import unittest
from datasets.GPT_4.Few_shot2.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_merge_dictionaries_non_overlapping(self): self.assertEqual(merge_dictionaries({'red': 2}, {'blue': 3}), {'red': 2, 'blue': 3})

    def test_merge_dictionaries_overlapping_keys(self): self.assertEqual(merge_dictionaries({'red': 2}, {'red': 3}), {'red': 5})

    def test_merge_dictionaries_both_empty(self): self.assertEqual(merge_dictionaries({}, {}), {})

    def test_merge_dictionaries_one_empty(self): self.assertEqual(merge_dictionaries({'green': 4}, {}), {'green': 4}); self.assertEqual(merge_dictionaries({}, {'green': 4}), {'green': 4})

    def test_merge_dictionaries_multiple_keys(self): self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 5, 'c': 4})

    def test_merge_dictionaries_zero_counts(self): self.assertEqual(merge_dictionaries({'x': 0}, {'x': 0}), {'x': 0})

    def test_merge_dictionaries_negative_counts(self): self.assertEqual(merge_dictionaries({'x': -1}, {'x': 3}), {'x': 2})

    def test_merge_dictionaries_large_counts(self): self.assertEqual(merge_dictionaries({'k': 100000}, {'k': 234567}), {'k': 334567})

    def test_merge_dictionaries_mixed_keys(self): self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'a': 4}), {'a': 5, 'b': 2, 'c': 3})

