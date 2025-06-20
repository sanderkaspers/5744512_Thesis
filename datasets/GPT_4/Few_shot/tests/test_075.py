import unittest
from datasets.GPT_4.Few_shot.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6) # All negative numbers)

    def test_case_2(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0) # No negative numbers)

    def test_case_3(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4]), -4) # Mixed positive and negative)

    def test_case_4(self):
        self.assertEqual(sum_negativenum([]), 0) # Empty list)

    def test_case_5(self):
        self.assertEqual(sum_negativenum([-1, -1, -1]), -3) # Repeated negative numbers)

    def test_case_6(self):
        self.assertEqual(sum_negativenum([0, -1, 1]), -1) # Zero and negative)

    def test_case_7(self):
        self.assertEqual(sum_negativenum([-10, -20, -30]), -60) # Large negative numbers)

    def test_case_8(self):
        self.assertEqual(sum_negativenum([10, -10, 20, -20]), -30) # Mixed with larger numbers)

