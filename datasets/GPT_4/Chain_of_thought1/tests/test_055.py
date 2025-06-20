import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_two_sorted_lists(self): self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_one_empty(self): self.assertEqual(merge_sorted_list([], [1, 2, 3]), [1, 2, 3]); self.assertEqual(merge_sorted_list([1, 2, 3], []), [1, 2, 3])

    def test_both_empty(self): self.assertEqual(merge_sorted_list([], []), [])

    def test_duplicates(self): self.assertEqual(merge_sorted_list([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

    def test_negatives(self): self.assertEqual(merge_sorted_list([-3, -1, 0], [-2, 1]), [-3, -2, -1, 0, 1])

    def test_floats(self): self.assertEqual(merge_sorted_list([1.1, 2.2], [1.5, 2.5]), [1.1, 1.5, 2.2, 2.5])

    def test_unequal_lengths(self): self.assertEqual(merge_sorted_list([1], [2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_left_smaller(self): self.assertEqual(merge_sorted_list([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_interleaved_values(self): self.assertEqual(merge_sorted_list([1, 4, 7], [2, 3, 6]), [1, 2, 3, 4, 6, 7])

    def test_unsorted_inputs(self): self.assertEqual(merge_sorted_list([3, 1], [4, 2]), [3, 1, 4, 2])

