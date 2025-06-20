import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_tuple_with_only_lists(self): self.assertEqual(find_lists(([1], [2], [3])), 3)

    def test_tuple_with_no_lists(self): self.assertEqual(find_lists((1, 2, 3)), 0)

    def test_tuple_with_mixed_types(self): self.assertEqual(find_lists(([1], 'text', 5, [2, 3])), 2)

    def test_empty_tuple(self): self.assertEqual(find_lists(()), 0)

    def test_tuple_with_nested_list_in_tuple(self): self.assertEqual(find_lists((([1, 2],),)), 0)

    def test_list_in_a_list_inside_tuple(self): self.assertEqual(find_lists(([[1, 2]],)), 1)

    def test_input_is_list(self): self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_tuple_with_none_and_lists(self): self.assertEqual(find_lists((None, [1], None)), 1)

