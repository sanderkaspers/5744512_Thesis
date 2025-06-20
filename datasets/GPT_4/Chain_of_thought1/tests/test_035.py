import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_disjoint_keys(self): self.assertEqual(merge_dictionaries({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

    def test_one_common_key(self): self.assertEqual(merge_dictionaries({'a': 1}, {'a': 2}), {'a': 3})

    def test_multiple_common_keys(self): self.assertEqual(merge_dictionaries({'x': 1, 'y': 2}, {'x': 3, 'y': 4, 'z': 5}), {'x': 4, 'y': 6, 'z': 5})

    def test_one_empty(self): self.assertEqual(merge_dictionaries({}, {'a': 2}), {'a': 2})

    def test_both_empty(self): self.assertEqual(merge_dictionaries({}, {}), {})

    def test_zero_values(self): self.assertEqual(merge_dictionaries({'a': 0}, {'a': 0}), {'a': 0})

    def test_negative_values(self): self.assertEqual(merge_dictionaries({'a': -2}, {'a': 5}), {'a': 3})

