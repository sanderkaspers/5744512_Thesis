import unittest
from datasets.GPT_4.Few_shot.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(closest_num(10), 9) # Positive integer)

    def test_case_2(self):
        self.assertEqual(closest_num(1), 0) # Edge case for smallest positive integer)

    def test_case_3(self):
        self.assertEqual(closest_num(0), -1) # Edge case for zero)

    def test_case_4(self):
        self.assertEqual(closest_num(-1), -2) # Negative integer)

    def test_case_5(self):
        self.assertEqual(closest_num(1000000), 999999) # Large positive integer)

    def test_case_6(self):
        self.assertEqual(closest_num(-1000000), -1000001) # Large negative integer)

    def test_case_7(self):
        self.assertEqual(closest_num(9999), 9998) # Four-digit positive integer)

    def test_case_8(self):
        self.assertEqual(closest_num(-9999), -10000) # Four-digit negative integer)

