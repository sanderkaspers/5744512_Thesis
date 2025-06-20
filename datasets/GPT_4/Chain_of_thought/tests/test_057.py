import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [2, 3, 5]]), [2, 3])

    def test_no_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [])

    def test_single_list(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3]]), [1, 2, 3])

    def test_empty_nested_list(self):
        self.assertEqual(common_in_nested_lists([]), [])

    def test_one_empty_list(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [], [2, 3, 4]]), [])

    def test_all_empty_lists(self):
        self.assertEqual(common_in_nested_lists([[], [], []]), [])

    def test_lists_with_duplicates(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 2, 3], [2, 2, 4, 5], [2, 3, 6]]), [2])

    def test_lists_with_different_data_types(self):
        self.assertEqual(common_in_nested_lists([[1, 'a', 3.5], ['a', 2, 3.5], [3.5, 'a', 4]]), ['a', 3.5])

    def test_lists_with_special_characters(self):
        self.assertEqual(common_in_nested_lists([['@', '#', '$'], ['$', '%', '&'], ['$', '!', '@']]), ['$'])

    def test_large_nested_lists(self):
        large_list = [[i for i in range(1000)] for _ in range(3)]
        self.assertEqual(common_in_nested_lists(large_list), list(range(1000)))

