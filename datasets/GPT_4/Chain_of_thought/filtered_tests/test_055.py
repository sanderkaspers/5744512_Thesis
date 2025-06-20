import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [0, 7, 8]), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_unsorted_lists(self):
        self.assertEqual(merge_sorted_list([5, 1, 3], [6, 2, 4], [8, 0, 7]), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [2, 4, 6], [1, 3, 5]), [1, 2, 3, 4, 5, 6])

    def test_all_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [], []), [])

    def test_lists_with_duplicates(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [3, 3, 6], [1, 7, 8]), [1, 1, 3, 3, 3, 5, 6, 7, 8])

    def test_lists_with_negative_values(self):
        self.assertEqual(merge_sorted_list([-5, -3, -1], [-6, -2, -4], [-8, 0, 7]), [-8, -6, -5, -4, -3, -2, -1, 0, 7])

    def test_mixed_positive_and_negative_values(self):
        self.assertEqual(merge_sorted_list([-5, 3, 1], [6, -2, 4], [8, 0, -7]), [-7, -5, -2, 0, 1, 3, 4, 6, 8])

    def test_single_element_lists(self):
        self.assertEqual(merge_sorted_list([1], [2], [3]), [1, 2, 3])

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            merge_sorted_list([1, 'two', 3], [4.5, 6], [7, 8.0, 'nine'])

    def test_large_lists(self):
        large_list1 = list(range(10000))
        large_list2 = list(range(10000, 20000))
        large_list3 = list(range(20000, 30000))
        self.assertEqual(merge_sorted_list(large_list1, large_list2, large_list3), list(range(30000)))

