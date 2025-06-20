import unittest
from datasets.GPT_4.Few_shot1.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_merge_dictionaries_basic(self): self.assertEqual(merge_dictionaries([{'a': 1}, {'a': 2}]), {'a': 3})

    def test_merge_dictionaries_multiple_keys(self): self.assertEqual(merge_dictionaries([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]), {'a': 1, 'b': 5, 'c': 4})

    def test_merge_dictionaries_empty_list(self): self.assertEqual(merge_dictionaries([]), {})

    def test_merge_dictionaries_single_dict(self): self.assertEqual(merge_dictionaries([{'x': 10}]), {'x': 10})

    def test_merge_dictionaries_disjoint_keys(self): self.assertEqual(merge_dictionaries([{'a': 1}, {'b': 2}]), {'a': 1, 'b': 2})

    def test_merge_dictionaries_with_zeros(self): self.assertEqual(merge_dictionaries([{'a': 0}, {'a': 0}]), {'a': 0})

    def test_merge_dictionaries_negative_values(self): self.assertEqual(merge_dictionaries([{'a': -1}, {'a': 2}]), {'a': 1})

