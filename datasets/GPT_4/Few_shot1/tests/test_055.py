import unittest
from datasets.GPT_4.Few_shot1.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_merge_sorted_list_basic(self): self.assertEqual(merge_sorted_list([1, 3], [2, 4], [5]), [1, 2, 3, 4, 5])

    def test_merge_sorted_list_unsorted_input(self): self.assertEqual(merge_sorted_list([4, 2], [3, 1], [6]), [1, 2, 3, 4, 6])

    def test_merge_sorted_list_empty_lists(self): self.assertEqual(merge_sorted_list([], [], []), [])

    def test_merge_sorted_list_one_empty(self): self.assertEqual(merge_sorted_list([3, 1], [], [2]), [1, 2, 3])

    def test_merge_sorted_list_duplicates(self): self.assertEqual(merge_sorted_list([1, 2], [2, 3], [1]), [1, 1, 2, 2, 3])

    def test_merge_sorted_list_single_elements(self): self.assertEqual(merge_sorted_list([5], [2], [3]), [2, 3, 5])

    def test_merge_sorted_list_negative_numbers(self): self.assertEqual(merge_sorted_list([-1, -3], [0], [-2]), [-3, -2, -1, 0])

