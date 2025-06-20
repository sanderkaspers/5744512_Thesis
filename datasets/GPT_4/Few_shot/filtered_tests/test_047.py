import unittest
from datasets.GPT_4.Few_shot.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(decimal_to_binary(5), "101") # Positive integer)

    def test_case_2(self):
        self.assertEqual(decimal_to_binary(0), "0") # Zero)

    def test_case_3(self):
        self.assertEqual(decimal_to_binary(10), "1010") # Another positive integer)

    def test_case_4(self):
        self.assertEqual(decimal_to_binary(255), "11111111") # Larger integer)

    def test_case_5(self):
        self.assertEqual(decimal_to_binary(1), "1") # Smallest positive integer)

    def test_case_6(self):
        self.assertEqual(decimal_to_binary(-5), "-101") # Negative integer)

    def test_case_7(self):
        self.assertEqual(decimal_to_binary(-1), "-1") # Edge case for -1)

    def test_case_8(self):
        self.assertEqual(decimal_to_binary(1024), "10000000000") # Power of two)

