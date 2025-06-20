import unittest
from datasets.GPT_4.Few_shot.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15) # Positive numbers)

    def test_case_2(self):
        self.assertEqual(count([-1, -2, -3, -4, -5]), -15) # Negative numbers)

    def test_case_3(self):
        self.assertEqual(count([1, -2, 3, -4, 5]), 3) # Mixed numbers)

    def test_case_4(self):
        self.assertEqual(count([]), 0) # Empty list)

    def test_case_5(self):
        self.assertEqual(count([0, 0, 0, 0]), 0) # All zeros)

    def test_case_6(self):
        self.assertEqual(count([1, 2, 3, -6]), 0) # Sums to zero)

    def test_case_7(self):
        self.assertEqual(count([10, 20, 30, 40]), 100) # Larger numbers)

    def test_case_8(self):
        self.assertEqual(count([-10, 10, -10, 10]), 0) # Alternating positive and negative)

