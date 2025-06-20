import unittest
from datasets.GPT_4.Few_shot2.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_add_lists_normal(self): self.assertEqual(add_lists([1, 2], (3, 4)), [1, 2, 3, 4])

    def test_add_lists_empty_list(self): self.assertEqual(add_lists([], (5, 6)), [5, 6])

    def test_add_lists_empty_tuple(self): self.assertEqual(add_lists([7, 8], ()), [7, 8])

    def test_add_lists_both_empty(self): self.assertEqual(add_lists([], ()), [])

    def test_add_lists_nested_elements(self): self.assertEqual(add_lists([[1], [2]], ((3,), (4,))), [[1], [2], (3,), (4,)])

    def test_add_lists_mixed_types(self): self.assertEqual(add_lists([1, 'a'], ('b', 2.5)), [1, 'a', 'b', 2.5])

    def test_add_lists_boolean_values(self): self.assertEqual(add_lists([True, False], (False, True)), [True, False, False, True])

