import unittest
from datasets.GPT_4.Few_shot.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(next_power_of_2(5), 8) # Next power of 2 greater than 5)

    def test_case_2(self):
        self.assertEqual(next_power_of_2(16), 16) # n is already a power of 2)

    def test_case_3(self):
        self.assertEqual(next_power_of_2(1), 1) # Smallest power of 2)

    def test_case_4(self):
        self.assertEqual(next_power_of_2(7), 8) # Next power of 2 greater than 7)

    def test_case_5(self):
        self.assertEqual(next_power_of_2(0), 1) # Edge case with n = 0)

    def test_case_6(self):
        self.assertEqual(next_power_of_2(1023), 1024) # Large number)

    def test_case_7(self):
        self.assertEqual(next_power_of_2(9), 16) # Next power of 2 greater than 9)

    def test_case_8(self):
        self.assertEqual(next_power_of_2(63), 64) # Power of 2 boundary case)

