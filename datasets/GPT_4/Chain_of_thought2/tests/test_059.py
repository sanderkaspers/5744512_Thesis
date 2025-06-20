import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_all_empty_dicts(self): self.assertTrue(empty_dit([{}, {}, {}]))

    def test_some_non_empty_dicts(self): self.assertFalse(empty_dit([{}, {'a': 1}, {}]))

    def test_single_empty_dict(self): self.assertTrue(empty_dit([{}]))

    def test_single_non_empty_dict(self): self.assertFalse(empty_dit([{'x': 42}]))

    def test_empty_list(self): self.assertTrue(empty_dit([]))

    def test_dict_with_nested_empty_dict(self): self.assertFalse(empty_dit([{'a': {}}]))

    def test_dict_with_falsey_value(self): self.assertFalse(empty_dit([{'a': 0}]))

    def test_non_dict_elements(self): self.assertFalse(empty_dit([{}, [], {}]))

    def test_all_non_dict_elements(self): self.assertFalse(empty_dit([[], '', 0]))

