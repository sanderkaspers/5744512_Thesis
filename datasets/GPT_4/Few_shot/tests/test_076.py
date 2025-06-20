import unittest
from datasets.GPT_4.Few_shot.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hexagonal_num(1), 1) # Smallest hexagonal number)

    def test_case_2(self):
        self.assertEqual(hexagonal_num(2), 6) # Second hexagonal number)

    def test_case_3(self):
        self.assertEqual(hexagonal_num(3), 15) # Third hexagonal number)

    def test_case_4(self):
        self.assertEqual(hexagonal_num(10), 190) # Larger n)

    def test_case_5(self):
        self.assertEqual(hexagonal_num(100), 19700) # Even larger n)

    def test_case_6(self):
        self.assertEqual(hexagonal_num(0), 0) # Edge case for n = 0)

    def test_case_7(self):
        try:
            hexagonal_num(-1)   # Negative n
        except ValueError:
            print("Passed: ValueError for negative n.")

    def test_case_8(self):
        self.assertEqual(hexagonal_num(50), 4950) # Large n, mid-range)

