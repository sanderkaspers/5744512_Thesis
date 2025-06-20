import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_list_input(self): self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_string_input(self): self.assertEqual(find_lists('abc'), 3)

    def test_tuple_input(self): self.assertEqual(find_lists((1, 2)), 2)

    def test_dict_input(self): self.assertEqual(find_lists({'a': 1, 'b': 2}), 2)

    def test_set_input(self): self.assertEqual(find_lists({1, 2, 3}), 3)

    def test_empty_list(self): self.assertEqual(find_lists([]), 1)

    def test_empty_string(self): self.assertEqual(find_lists(''), 0)

    def test_nested_list(self): self.assertEqual(find_lists([[1], [2]]), 1)

