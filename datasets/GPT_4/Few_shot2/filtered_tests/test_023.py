import unittest
from datasets.GPT_4.Few_shot2.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_comb_sort_basic(self): self.assertEqual(comb_sort([3, 1, 2]), [1, 2, 3])

    def test_comb_sort_already_sorted(self): self.assertEqual(comb_sort([1, 2, 3]), [1, 2, 3])

    def test_comb_sort_reverse_order(self): self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_comb_sort_with_duplicates(self): self.assertEqual(comb_sort([4, 5, 4, 3]), [3, 4, 4, 5])

    def test_comb_sort_empty_list(self): self.assertEqual(comb_sort([]), [])

    def test_comb_sort_single_element(self): self.assertEqual(comb_sort([7]), [7])

    def test_comb_sort_all_equal(self): self.assertEqual(comb_sort([2, 2, 2]), [2, 2, 2])

    def test_comb_sort_negative_numbers(self): self.assertEqual(comb_sort([-1, -3, -2]), [-3, -2, -1])

    def test_comb_sort_mixed_numbers(self): self.assertEqual(comb_sort([3, -1, 0, 5, 2]), [-1, 0, 2, 3, 5])

