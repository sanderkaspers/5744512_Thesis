import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_lists(([], [1, 2], [3, 4, 5])), 3)

    def test_no_lists(self):
        self.assertEqual(find_lists((1, 2, 'string')), 0)

    def test_all_lists(self):
        self.assertEqual(find_lists(([], [], [])), 3)

    def test_nested_lists(self):
        self.assertEqual(find_lists(([], [1, [2, 3]], [[4, 5], 6])), 3)

    def test_single_element_tuple(self):
        self.assertEqual(find_lists(([1, 2, 3],)), 1)

    def test_empty_tuple(self):
        self.assertEqual(find_lists(()), 0)

    def test_mixed_data_types(self):
        self.assertEqual(find_lists(([], 'string', 3, [1, 2], None)), 2)

    def test_list_as_input(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_tuple_with_none(self):
        self.assertEqual(find_lists((None, [1, 2, 3])), 1)

    def test_repeated_lists(self):
        lst = [1, 2, 3]
        self.assertEqual(find_lists((lst, lst, lst)), 3)

