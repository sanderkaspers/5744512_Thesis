import unittest
from datasets.GPT_4.Few_shot2.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_pancake_sort_unsorted(self): self.assertEqual(pancake_sort([3, 2, 4, 1]), [1, 2, 3, 4])

    def test_pancake_sort_already_sorted(self): self.assertEqual(pancake_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_pancake_sort_reverse_sorted(self): self.assertEqual(pancake_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_pancake_sort_with_duplicates(self): self.assertEqual(pancake_sort([3, 1, 2, 3]), [1, 2, 3, 3])

    def test_pancake_sort_single_element(self): self.assertEqual(pancake_sort([5]), [5])

    def test_pancake_sort_two_elements(self): self.assertEqual(pancake_sort([2, 1]), [1, 2])

    def test_pancake_sort_empty_list(self): self.assertEqual(pancake_sort([]), [])

    def test_pancake_sort_large_list(self): self.assertEqual(pancake_sort([9, 7, 5, 3, 1, 2, 4, 6, 8, 10]), list(range(1, 11)))

