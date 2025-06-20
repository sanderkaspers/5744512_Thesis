import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_all_empty_dictionaries(self):
        self.assertTrue(empty_dit([{}, {}, {}]))

    def test_non_empty_dictionaries(self):
        self.assertFalse(empty_dit([{}, {'a': 1}, {}]))

    def test_mixed_empty_and_non_empty_dictionaries(self):
        self.assertFalse(empty_dit([{}, {'a': 1}, {'b': 2}]))

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_no_dictionaries(self):
        self.assertTrue(empty_dit(['string', 123, []]))

    def test_nested_dictionaries(self):
        self.assertFalse(empty_dit([{'a': {'b': {}}}, {}]))

    def test_single_dictionary(self):
        self.assertTrue(empty_dit([{}]))
        self.assertFalse(empty_dit([{'a': 1}]))

    def test_duplicate_dictionaries(self):
        self.assertTrue(empty_dit([{}, {}, {}]))
        self.assertFalse(empty_dit([{}, {'a': 1}, {'a': 1}]))

    def test_large_list_of_dictionaries(self):
        self.assertTrue(empty_dit([{} for _ in range(10000)]))
        self.assertFalse(empty_dit([{} for _ in range(9999)] + [{'a': 1}]))

    def test_none_in_list(self):
        self.assertTrue(empty_dit([{}, None, {}]))
        self.assertFalse(empty_dit([{}, None, {'a': 1}]))

