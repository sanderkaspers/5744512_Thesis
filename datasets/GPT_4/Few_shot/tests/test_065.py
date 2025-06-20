import unittest
from datasets.GPT_4.Few_shot.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(amicable_numbers_sum(1000), 504) # Standard case)

    def test_case_2(self):
        self.assertEqual(amicable_numbers_sum(1), 0) # Limit with no amicable numbers)

    def test_case_3(self):
        self.assertEqual(amicable_numbers_sum(300), 220) # Smaller limit)

    def test_case_4(self):
        self.assertEqual(amicable_numbers_sum(0), 0) # Edge case limit = 0)

    def test_case_5(self):
        self.assertEqual(amicable_numbers_sum(-100), 0) # Negative limit)

    def test_case_6(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626) # Larger limit)

    def test_case_7(self):
        self.assertEqual(amicable_numbers_sum(220), 0) # Edge limit with one amicable pair)

    def test_case_8(self):
        self.assertEqual(amicable_numbers_sum(200), 0) # Limit just below first amicable number pair)

