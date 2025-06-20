import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_unsorted(self): self.assertEqual(pancake_sort([3, 2, 4, 1]), [1, 2, 3, 4])

    def test_sorted(self): self.assertEqual(pancake_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_sorted(self): self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_single_element(self): self.assertEqual(pancake_sort([5]), [5])

    def test_two_elements(self): self.assertEqual(pancake_sort([2, 1]), [1, 2])

    def test_with_duplicates(self): self.assertEqual(pancake_sort([3, 1, 2, 1]), sorted([3, 1, 2, 1]))

    def test_empty_list(self): self.assertEqual(pancake_sort([]), [])

    def test_negative_numbers(self): self.assertEqual(pancake_sort([-3, -1, -2]), [-3, -2, -1])

    def test_mixed_numbers(self): self.assertEqual(pancake_sort([1.5, 0, 3.2]), sorted([1.5, 0, 3.2]))

    def test_large_list(self): import random; input_list = list(range(100)); random.shuffle(input_list); self.assertEqual(pancake_sort(input_list), list(range(100)))

