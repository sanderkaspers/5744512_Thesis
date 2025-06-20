import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_unsorted_middle(self): self.assertEqual(kth_element([4, 1, 3, 2], 2), 2)

    def test_sorted_list(self): self.assertEqual(kth_element([1, 2, 3, 4], 3), 3)

    def test_descending_list(self): self.assertEqual(kth_element([5, 4, 3, 2, 1], 1), 1)

    def test_with_duplicates(self): self.assertEqual(kth_element([3, 1, 2, 2], 3), 2)

    def test_k_is_1(self): self.assertEqual(kth_element([10, 5, 2], 1), 2)

    def test_k_is_length(self): self.assertEqual(kth_element([7, 8, 9], 3), 9)

    def test_negative_numbers(self): self.assertEqual(kth_element([-5, -2, -3, -1], 2), -3)

    def test_single_element(self): self.assertEqual(kth_element([42], 1), 42)

