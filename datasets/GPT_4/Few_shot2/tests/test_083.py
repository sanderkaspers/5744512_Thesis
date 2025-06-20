import unittest
from datasets.GPT_4.Few_shot2.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_find_lists_with_list(self): self.assertEqual(find_lists([1, 2]), [[1, 2]])

    def test_find_lists_with_empty_list(self): self.assertEqual(find_lists([]), [[]])

    def test_find_lists_with_string(self): self.assertEqual(find_lists('not a list'), [])

    def test_find_lists_with_tuple(self): self.assertEqual(find_lists((1, 2)), [])

    def test_find_lists_with_dict(self): self.assertEqual(find_lists({'a': 1}), [])

    def test_find_lists_with_set(self): self.assertEqual(find_lists({1, 2}), [])

    def test_find_lists_with_integer(self): self.assertEqual(find_lists(5), [])

    def test_find_lists_with_none(self): self.assertEqual(find_lists(None), [])

    def test_find_lists_nested_list(self): self.assertEqual(find_lists([[1, 2]]), [[[1, 2]]])

