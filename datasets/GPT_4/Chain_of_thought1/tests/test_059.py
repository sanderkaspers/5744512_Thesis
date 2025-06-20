import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_all_empty_dicts(self): self.assertTrue(empty_dit([{}, {}, {}]))

    def test_one_non_empty(self): self.assertFalse(empty_dit([{}, {'a': 1}, {}]))

    def test_single_empty_dict(self): self.assertTrue(empty_dit([{}]))

    def test_single_non_empty_dict(self): self.assertFalse(empty_dit([{'x': 1}]))

    def test_empty_list(self): self.assertTrue(empty_dit([]))

    def test_large_empty_list(self): self.assertTrue(empty_dit([{}] * 1000))

    def test_non_dict_element(self): self.assertFalse(empty_dit([{}, [], {}]))

    def test_none_in_list(self): self.assertFalse(empty_dit([{}, None, {}]))

    def test_false_value(self): self.assertFalse(empty_dit([{'a': False}]))

    def test_nested_empty_dict(self): self.assertFalse(empty_dit([{'a': {}}, {}]))

    def test_list_with_set_and_dict(self): self.assertFalse(empty_dit([{}, set(), {}]))

