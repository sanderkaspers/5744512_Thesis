import unittest
from datasets.o3.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_int(5,3), 15)

    def test_zero_multiplier(self):
        self.assertEqual(multiply_int(7,0), 0)

    def test_negative_multiplier(self):
        self.assertEqual(multiply_int(4,-3), -12)

    def test_negative_multiplicand(self):
        self.assertEqual(multiply_int(-4,3), -12)

    def test_both_negative(self):
        self.assertEqual(multiply_int(-2,-3), 6)

