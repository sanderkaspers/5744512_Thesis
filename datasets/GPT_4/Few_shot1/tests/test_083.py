import unittest
from datasets.GPT_4.Few_shot1.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_find_lists_with_list(self): self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_find_lists_with_empty_list(self): self.assertEqual(find_lists([]), 1)

    def test_find_lists_with_string(self): self.assertEqual(find_lists("hello"), 5)

    def test_find_lists_with_empty_string(self): self.assertEqual(find_lists(""), 0)

    def test_find_lists_with_tuple(self): self.assertEqual(find_lists((1, 2, 3)), 3)

    def test_find_lists_with_dict(self): self.assertEqual(find_lists({'a': 1, 'b': 2}), 2)

    def test_find_lists_with_set(self): self.assertEqual(find_lists({1, 2, 3}), 3)

    def test_find_lists_with_nested_list(self): self.assertEqual(find_lists([[1], [2]]), 1)

