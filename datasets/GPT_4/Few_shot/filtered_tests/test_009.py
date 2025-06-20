import unittest
from datasets.GPT_4.Few_shot.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(rev(123), 321)

    def test_case_2(self):
        self.assertEqual(rev(100), 1) # Trailing zeros should be omitted)

    def test_case_3(self):
        self.assertEqual(rev(0), 0) # Edge case for zero)

    def test_case_4(self):
        self.assertEqual(rev(9), 9) # Single-digit number)

    def test_case_5(self):
        self.assertEqual(rev(123456789), 987654321) # Large number)

    def test_case_6(self):
        self.assertEqual(rev(120), 21) # Edge case with trailing zero)

    def test_case_7(self):
        self.assertEqual(rev(1000000), 1) # Multiple trailing zeros)

    def test_case_8(self):
        self.assertEqual(rev(56), 65) # Normal case)

