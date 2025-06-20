import unittest
from datasets.GPT_4.Few_shot2.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_sort_sublists_basic(self): self.assertEqual(sort_sublists([[3, 1], [2, 4]]), [[1, 3], [2, 4]])

    def test_sort_sublists_with_negatives(self): self.assertEqual(sort_sublists([[0, -1], [-2, 2]]), [[-1, 0], [-2, 2]])

    def test_sort_sublists_empty_outer(self): self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_empty_inner_lists(self): self.assertEqual(sort_sublists([[], []]), [[], []])

    def test_sort_sublists_mixed_lengths(self): self.assertEqual(sort_sublists([[3], [2, 1, 4]]), [[3], [1, 2, 4]])

    def test_sort_sublists_duplicates(self): self.assertEqual(sort_sublists([[1, 1], [2, 2]]), [[1, 1], [2, 2]])

    def test_sort_sublists_already_sorted(self): self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_sort_sublists_reverse_sorted(self): self.assertEqual(sort_sublists([[3, 2, 1], [5, 4]]), [[1, 2, 3], [4, 5]])

    def test_sort_sublists_single_inner_list(self): self.assertEqual(sort_sublists([[4, 3, 2, 1]]), [[1, 2, 3, 4]])

