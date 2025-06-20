import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_elements([1, 2, 3, 4], [2, 4, 6]), [1, 3])

    def test_no_common_elements(self):
        self.assertEqual(remove_elements([1, 2, 3], [4, 5, 6]), [1, 2, 3])

    def test_all_elements_common(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3]), [])

    def test_empty_list1(self):
        self.assertEqual(remove_elements([], [1, 2, 3]), [])

    def test_empty_list2(self):
        self.assertEqual(remove_elements([1, 2, 3], []), [1, 2, 3])

    def test_both_lists_empty(self):
        self.assertEqual(remove_elements([], []), [])

    def test_lists_with_duplicates(self):
        self.assertEqual(remove_elements([1, 2, 2, 3], [2]), [1, 3])

    def test_different_data_types(self):
        self.assertEqual(remove_elements([1, '2', 3.0], ['2', 3]), [1, 3.0])

    def test_large_lists(self):
        list1 = list(range(10000))
        list2 = list(range(5000, 15000))
        expected = list(range(5000))
        self.assertEqual(remove_elements(list1, list2), expected)

    def test_sublist_relationship(self):
        self.assertEqual(remove_elements([1, 2], [1, 2, 3, 4]), [])

