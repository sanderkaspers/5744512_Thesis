import unittest
from datasets.GPT_4.Few_shot.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(opposite_Signs(10, -10), True) # Positive and negative)

    def test_case_2(self):
        self.assertEqual(opposite_Signs(-5, 5), True) # Negative and positive)

    def test_case_3(self):
        self.assertEqual(opposite_Signs(0, 5), False) # Zero and positive)

    def test_case_4(self):
        self.assertEqual(opposite_Signs(0, -5), True) # Zero and negative)

    def test_case_5(self):
        self.assertEqual(opposite_Signs(10, 10), False) # Both positive)

    def test_case_6(self):
        self.assertEqual(opposite_Signs(-10, -10), False) # Both negative)

    def test_case_7(self):
        self.assertEqual(opposite_Signs(1, 1), False) # Small positive numbers)

    def test_case_8(self):
        self.assertEqual(opposite_Signs(-1, 1), True) # Small negative and positive)

