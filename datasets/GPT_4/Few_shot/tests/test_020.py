import unittest
from datasets.GPT_4.Few_shot.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_Monotonic([1, 2, 3, 4, 5]), True) # Strictly increasing)

    def test_case_2(self):
        self.assertEqual(is_Monotonic([5, 4, 3, 2, 1]), True) # Strictly decreasing)

    def test_case_3(self):
        self.assertEqual(is_Monotonic([3, 3, 3, 3, 3]), True) # Constant values)

    def test_case_4(self):
        self.assertEqual(is_Monotonic([1, 2, 3, 2, 1]), False) # Mixed list)

    def test_case_5(self):
        self.assertEqual(is_Monotonic([]), True) # Empty list)

    def test_case_6(self):
        self.assertEqual(is_Monotonic([1]), True) # Single element list)

    def test_case_7(self):
        self.assertEqual(is_Monotonic([2, 2, 3, 4, 4, 5]), True) # Non-decreasing with repeats)

    def test_case_8(self):
        self.assertEqual(is_Monotonic([5, 4, 4, 3, 2, 2]), True) # Non-increasing with repeats)

