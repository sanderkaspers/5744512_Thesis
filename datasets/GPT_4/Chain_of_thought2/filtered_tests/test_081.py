import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_sorted_list(self): self.assertEqual(pancake_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_sorted_list(self): self.assertEqual(pancake_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted_list(self): self.assertEqual(pancake_sort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_list_with_duplicates(self): self.assertEqual(pancake_sort([3, 1, 2, 3]), [1, 2, 3, 3])

    def test_all_same_elements(self): self.assertEqual(pancake_sort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_empty_list(self): self.assertEqual(pancake_sort([]), [])

    def test_single_element_list(self): self.assertEqual(pancake_sort([42]), [42])

    def test_two_element_list_sorted(self): self.assertEqual(pancake_sort([1, 2]), [1, 2])

    def test_two_element_list_unsorted(self): self.assertEqual(pancake_sort([2, 1]), [1, 2])

    def test_negative_numbers(self): self.assertEqual(pancake_sort([-3, -1, -2]), [-3, -2, -1])

    def test_mixed_signed_integers(self): self.assertEqual(pancake_sort([0, -1, 2, -3]), [-3, -1, 0, 2])

    def test_list_with_floats(self): self.assertEqual(pancake_sort([3.1, 2.2, 5.5, 1.0]), [1.0, 2.2, 3.1, 5.5])

