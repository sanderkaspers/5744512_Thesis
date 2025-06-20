import unittest
from datasets.GPT_4.Few_shot.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 4) # All positive numbers)

    def test_case_2(self):
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5]), 4) # All negative numbers)

    def test_case_3(self):
        self.assertEqual(max_Abs_Diff([1, -2, 3, -4, 5]), 9) # Mixed positive and negative)

    def test_case_4(self):
        self.assertEqual(max_Abs_Diff([1]), 0) # Single element)

    def test_case_5(self):
        self.assertEqual(max_Abs_Diff([0, 0, 0, 0]), 0) # All zeros)

    def test_case_6(self):
        self.assertEqual(max_Abs_Diff([100, -100]), 200) # Two extreme values)

    def test_case_7(self):
        self.assertEqual(max_Abs_Diff([5, 1, 9, 7]), 8) # Non-sequential numbers)

    def test_case_8(self):
        self.assertEqual(max_Abs_Diff([10, 20, 30, 40]), 30) # Larger positive numbers)

