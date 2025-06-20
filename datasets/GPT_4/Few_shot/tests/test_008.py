import unittest
from datasets.GPT_4.Few_shot.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_woodall(1), False) # Not a Woodall number)

    def test_case_2(self):
        self.assertEqual(is_woodall(7), True) # Woodall number)

    def test_case_3(self):
        self.assertEqual(is_woodall(15), False) # Not a Woodall number)

    def test_case_4(self):
        self.assertEqual(is_woodall(-7), False) # Negative numbers not considered)

    def test_case_5(self):
        self.assertEqual(is_woodall(23), True) # Woodall number)

    def test_case_6(self):
        self.assertEqual(is_woodall(0), False) # Zero is not a Woodall number)

    def test_case_7(self):
        self.assertEqual(is_woodall(2), False) # Even number not a Woodall number)

    def test_case_8(self):
        self.assertEqual(is_woodall(31), True) # Woodall number)

