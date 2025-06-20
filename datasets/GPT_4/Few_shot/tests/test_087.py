import unittest
from datasets.GPT_4.Few_shot.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum_series(5), 15) # 1+2+3+4+5)

    def test_case_2(self):
        self.assertEqual(sum_series(1), 1) # Single element)

    def test_case_3(self):
        self.assertEqual(sum_series(10), 55) # Sum of first 10 numbers)

    def test_case_4(self):
        self.assertEqual(sum_series(0), 0) # Edge case n = 0)

    def test_case_5(self):
        self.assertEqual(sum_series(-5), 0) # Negative n)

    def test_case_6(self):
        self.assertEqual(sum_series(100), 5050) # Large n)

    def test_case_7(self):
        self.assertEqual(sum_series(2), 3) # Simple case n = 2)

    def test_case_8(self):
        self.assertEqual(sum_series(3), 6) # Simple case n = 3)

