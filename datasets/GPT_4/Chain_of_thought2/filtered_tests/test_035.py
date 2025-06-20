import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_non_overlapping_dicts(self): self.assertEqual(merge_dictionaries_three({'a': 1}, {'b': 2}, {'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_overlap_dict1_overrides(self): self.assertEqual(merge_dictionaries_three({'x': 1}, {'x': 2}, {'x': 3}), {'x': 1})

    def test_overlap_dict2_overrides_dict3(self): self.assertEqual(merge_dictionaries_three({}, {'y': 10}, {'y': 20}), {'y': 10})

    def test_one_empty_dict(self): self.assertEqual(merge_dictionaries_three({}, {'a': 2}, {'b': 3}), {'a': 2, 'b': 3})

    def test_all_empty_dicts(self): self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_same_key_all_levels(self): self.assertEqual(merge_dictionaries_three({'z': 100}, {'z': 200}, {'z': 300}), {'z': 100})

    def test_non_string_keys(self): self.assertEqual(merge_dictionaries_three({1: 'one'}, {(2, 3): 'tuple'}, {3.14: 'pi'}), {1: 'one', (2, 3): 'tuple', 3.14: 'pi'})

    def test_values_as_none(self): self.assertEqual(merge_dictionaries_three({'a': None}, {'b': 2}, {'c': 3}), {'a': None, 'b': 2, 'c': 3})

    def test_nested_dictionaries_as_values(self): self.assertEqual(merge_dictionaries_three({'a': {'x': 1}}, {'b': {'y': 2}}, {'c': {'z': 3}}), {'a': {'x': 1}, 'b': {'y': 2}, 'c': {'z': 3}})

