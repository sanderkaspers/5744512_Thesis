import unittest
from datasets.GPT_4.Few_shot.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_Diff(22), True) # Divisible by 11)

    def test_case_2(self):
        self.assertEqual(is_Diff(23), False) # Not divisible by 11)

    def test_case_3(self):
        self.assertEqual(is_Diff(0), True) # Zero is divisible by any number)

    def test_case_4(self):
        self.assertEqual(is_Diff(-11), True) # Negative number divisible by 11)

    def test_case_5(self):
        self.assertEqual(is_Diff(-22), True) # Negative number divisible by 11)

    def test_case_6(self):
        self.assertEqual(is_Diff(1), False) # Small positive number not divisible by 11)

    def test_case_7(self):
        self.assertEqual(is_Diff(-1), False) # Small negative number not divisible by 11)

    def test_case_8(self):
        self.assertEqual(is_Diff(121), True) # Large number divisible by 11)

