import unittest
from datasets.GPT_4.Few_shot.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 5]), 120) # Positive numbers)

    def test_case_2(self):
        self.assertEqual(multiply_num([1, 2, 0, 4, 5]), 0) # Contains zero)

    def test_case_3(self):
        self.assertEqual(multiply_num([1, -2, 3, -4, 5]), 120) # Mixed positive and negative numbers)

    def test_case_4(self):
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5]), -120) # All negative numbers)

    def test_case_5(self):
        self.assertEqual(multiply_num([2]), 2) # Single number)

    def test_case_6(self):
        self.assertEqual(multiply_num([]), 1) # Empty list, by convention multiplying nothing is 1)

    def test_case_7(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 0]), 0) # Zero at the end)

    def test_case_8(self):
        self.assertEqual(multiply_num([1, 1, 1, 1]), 1) # All ones)

