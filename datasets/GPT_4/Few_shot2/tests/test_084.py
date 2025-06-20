import unittest
from datasets.GPT_4.Few_shot2.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_max_Abs_Diff_regular(self): self.assertEqual(max_Abs_Diff([1, 2, 3]), 2)

    def test_max_Abs_Diff_same_elements(self): self.assertEqual(max_Abs_Diff([5, 5, 5]), 0)

    def test_max_Abs_Diff_single_element(self): self.assertEqual(max_Abs_Diff([10]), 0)

    def test_max_Abs_Diff_negative_values(self): self.assertEqual(max_Abs_Diff([-1, -5, -3]), 4)

    def test_max_Abs_Diff_mixed_signs(self): self.assertEqual(max_Abs_Diff([-10, 0, 10]), 20)

    def test_max_Abs_Diff_unsorted(self): self.assertEqual(max_Abs_Diff([7, 2, 9, 4]), 7)

    def test_max_Abs_Diff_large_range(self): self.assertEqual(max_Abs_Diff([1000, -1000]), 2000)

    def test_max_Abs_Diff_repeating_diff(self): self.assertEqual(max_Abs_Diff([3, 3, 6, 0]), 6)

    def test_max_Abs_Diff_zeroes(self): self.assertEqual(max_Abs_Diff([0, 0, 0]), 0)

