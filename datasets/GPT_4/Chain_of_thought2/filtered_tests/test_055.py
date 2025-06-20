import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_unsorted_integer_lists(self): self.assertEqual(merge_sorted_list([3, 1], [4, 2], [6, 5]), [1, 2, 3, 4, 5, 6])

    def test_lists_of_different_lengths(self): self.assertEqual(merge_sorted_list([1], [5, 3], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_with_duplicates(self): self.assertEqual(merge_sorted_list([1, 2], [2, 3], [3, 4]), [1, 2, 2, 3, 3, 4])

    def test_all_empty_lists(self): self.assertEqual(merge_sorted_list([], [], []), [])

    def test_some_empty_lists(self): self.assertEqual(merge_sorted_list([], [1, 3], [2]), [1, 2, 3])

    def test_negative_numbers(self): self.assertEqual(merge_sorted_list([-3, -1], [0], [-2, -4]), [-4, -3, -2, -1, 0])

    def test_sorted_input(self): self.assertEqual(merge_sorted_list([1, 3], [2, 4], [5, 6]), [1, 2, 3, 4, 5, 6])

    def test_mixed_floats_and_integers(self): self.assertEqual(merge_sorted_list([1.5, 2], [3, 0.5], [4]), [0.5, 1.5, 2, 3, 4])

