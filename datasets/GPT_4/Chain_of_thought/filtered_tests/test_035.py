import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_overlapping_keys_dict1_dict2(self):
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        dict3 = {'b': 3}
        expected = {'a': 1, 'b': 3}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_overlapping_keys_all_dicts(self):
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        dict3 = {'a': 3}
        expected = {'a': 1}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_one_empty_dictionary(self):
        dict1 = {}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        expected = {'b': 2, 'c': 3}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_all_empty_dictionaries(self):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        expected = {}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_different_data_types(self):
        dict1 = {'a': 1}
        dict2 = {'b': 'two'}
        dict3 = {'c': [3, 3, 3]}
        expected = {'a': 1, 'b': 'two', 'c': [3, 3, 3]}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_nested_dictionaries(self):
        dict1 = {'a': {'nested': 1}}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        expected = {'a': {'nested': 1}, 'b': 2, 'c': 3}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_large_dictionaries(self):
        dict1 = {i: i for i in range(1000)}
        dict2 = {i: i * 2 for i in range(1000, 2000)}
        dict3 = {i: i * 3 for i in range(2000, 3000)}
        merged = merge_dictionaries_three(dict1, dict2, dict3)
        self.assertEqual(len(merged), 3000)
        self.assertEqual(merged[0], 0)
        self.assertEqual(merged[1000], 2000)
        self.assertEqual(merged[2000], 6000)

    def test_identical_dictionaries(self):
        dict1 = {'a': 1}
        dict2 = {'a': 1}
        dict3 = {'a': 1}
        expected = {'a': 1}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_single_key_value_pair(self):
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

