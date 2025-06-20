import unittest
from datasets.GPT_4.Few_shot1.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_max_abs_diff_basic(self): self.assertEqual(max_Abs_Diff([1, 2, 3]), 2)

    def test_max_abs_diff_negative_values(self): self.assertEqual(max_Abs_Diff([-10, -20, -30]), 20)

    def test_max_abs_diff_mixed_values(self): self.assertEqual(max_Abs_Diff([-5, 0, 5]), 10)

    def test_max_abs_diff_all_same(self): self.assertEqual(max_Abs_Diff([4, 4, 4]), 0)

    def test_max_abs_diff_two_elements(self): self.assertEqual(max_Abs_Diff([10, 3]), 7)

    def test_max_abs_diff_single_element(self): self.assertEqual(max_Abs_Diff([7]), 0)

    def test_max_abs_diff_large_range(self): self.assertEqual(max_Abs_Diff([-1000, 500, 2000]), 3000)

    def test_max_abs_diff_ordered(self): self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 4)

    def test_max_abs_diff_reverse_ordered(self): self.assertEqual(max_Abs_Diff([5, 4, 3, 2, 1]), 4)

    def test_max_abs_diff_large_input(self): self.assertEqual(max_Abs_Diff(list(range(-1000, 1001))), 2000)

