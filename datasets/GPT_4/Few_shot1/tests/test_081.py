import unittest
from datasets.GPT_4.Few_shot1.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_pancake_sort_basic(self): self.assertEqual(pancake_sort([3, 2, 4, 1]), [1, 2, 3, 4])

    def test_pancake_sort_sorted(self): self.assertEqual(pancake_sort([1, 2, 3]), [1, 2, 3])

    def test_pancake_sort_reverse(self): self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_pancake_sort_single_element(self): self.assertEqual(pancake_sort([7]), [7])

    def test_pancake_sort_two_elements(self): self.assertEqual(pancake_sort([2, 1]), [1, 2])

    def test_pancake_sort_with_duplicates(self): self.assertEqual(pancake_sort([3, 1, 2, 3]), [1, 2, 3, 3])

    def test_pancake_sort_all_same(self): self.assertEqual(pancake_sort([4, 4, 4]), [4, 4, 4])

    def test_pancake_sort_large_numbers(self): self.assertEqual(pancake_sort([100, 1, 99]), [1, 99, 100])

    def test_pancake_sort_negative_numbers(self): self.assertEqual(pancake_sort([-1, -3, -2]), [-3, -2, -1])

    def test_pancake_sort_empty(self): self.assertEqual(pancake_sort([]), [])

