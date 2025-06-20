import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_sorted_list(self): self.assertEqual(comb_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_sorted(self): self.assertEqual(comb_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted(self): self.assertEqual(comb_sort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_with_duplicates(self): self.assertEqual(comb_sort([4, 1, 2, 4, 3, 1]), [1, 1, 2, 3, 4, 4])

    def test_all_same(self): self.assertEqual(comb_sort([5, 5, 5]), [5, 5, 5])

    def test_floats(self): self.assertEqual(comb_sort([3.1, 2.2, 5.5, 1.1]), [1.1, 2.2, 3.1, 5.5])

    def test_single_element(self): self.assertEqual(comb_sort([7]), [7])

    def test_empty_list(self): self.assertEqual(comb_sort([]), [])

    def test_boolean_values(self): self.assertEqual(comb_sort([True, False, True]), [False, True, True])

    def test_in_place_mutation(self): data = [4, 1, 3]; ref = data; comb_sort(data); self.assertEqual(ref, [1, 3, 4])

