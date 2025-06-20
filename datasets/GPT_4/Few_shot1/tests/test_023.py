import unittest
from datasets.GPT_4.Few_shot1.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_comb_sort_empty_list(self): self.assertEqual(comb_sort([]), [])

    def test_comb_sort_single_element(self): self.assertEqual(comb_sort([5]), [5])

    def test_comb_sort_already_sorted(self): self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_comb_sort_reverse_order(self): self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_comb_sort_with_duplicates(self): self.assertEqual(comb_sort([4, 2, 4, 3, 1]), [1, 2, 3, 4, 4])

    def test_comb_sort_all_same(self): self.assertEqual(comb_sort([7, 7, 7]), [7, 7, 7])

    def test_comb_sort_with_negatives(self): self.assertEqual(comb_sort([-1, -3, 2, 0]), [-3, -1, 0, 2])

    def test_comb_sort_with_floats(self): self.assertEqual(comb_sort([3.1, 2.4, 5.6]), [2.4, 3.1, 5.6])

    def test_comb_sort_large_input(self): self.assertEqual(comb_sort(list(range(1000, 0, -1))), list(range(1, 1001)))

    def test_comb_sort_already_sorted_floats(self): self.assertEqual(comb_sort([1.1, 2.2, 3.3]), [1.1, 2.2, 3.3])

