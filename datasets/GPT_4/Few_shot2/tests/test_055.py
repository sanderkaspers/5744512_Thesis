import unittest
from datasets.GPT_4.Few_shot2.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_merge_sorted_list_basic(self): self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_sorted_list_one_empty(self): self.assertEqual(merge_sorted_list([], [1, 2, 3]), [1, 2, 3])

    def test_merge_sorted_list_both_empty(self): self.assertEqual(merge_sorted_list([], []), [])

    def test_merge_sorted_list_with_duplicates(self): self.assertEqual(merge_sorted_list([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

    def test_merge_sorted_list_all_identical(self): self.assertEqual(merge_sorted_list([1, 1], [1, 1]), [1, 1, 1, 1])

    def test_merge_sorted_list_reverse_inputs(self): self.assertEqual(merge_sorted_list([5, 6], [1, 2]), [1, 2, 5, 6])

    def test_merge_sorted_list_negatives(self): self.assertEqual(merge_sorted_list([-3, -1], [-2, 0]), [-3, -2, -1, 0])

    def test_merge_sorted_list_floats(self): self.assertEqual(merge_sorted_list([1.1, 2.2], [1.5, 2.0]), [1.1, 1.5, 2.0, 2.2])

    def test_merge_sorted_list_unsorted_inputs(self): self.assertEqual(merge_sorted_list([3, 1], [4, 2]), [1, 2, 3, 4])

    def test_merge_sorted_list_large(self): self.assertEqual(merge_sorted_list(list(range(1000)), list(range(1000, 2000))), list(range(2000)))

