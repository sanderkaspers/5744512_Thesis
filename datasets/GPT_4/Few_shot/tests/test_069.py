import unittest
from datasets.GPT_4.Few_shot.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(multiply_int(3, 4), 12) # Positive integers)

    def test_case_2(self):
        self.assertEqual(multiply_int(-3, 4), -12) # Negative and positive)

    def test_case_3(self):
        self.assertEqual(multiply_int(3, -4), -12) # Positive and negative)

    def test_case_4(self):
        self.assertEqual(multiply_int(-3, -4), 12) # Both negative)

    def test_case_5(self):
        self.assertEqual(multiply_int(0, 5), 0) # Zero multiplier)

    def test_case_6(self):
        self.assertEqual(multiply_int(0, 0), 0) # Both zero)

    def test_case_7(self):
        self.assertEqual(multiply_int(100, 200), 20000) # Large positive integers)

    def test_case_8(self):
        self.assertEqual(multiply_int(-100, 200), -20000) # Large negative and positive)

