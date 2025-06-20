import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_int(3, 4), 12)

    def test_negative_multiplier(self):
        self.assertEqual(multiply_int(3, -4), -12)

    def test_negative_multiplicand(self):
        self.assertEqual(multiply_int(-3, 4), -12)

    def test_both_negative(self):
        self.assertEqual(multiply_int(-3, -4), 12)

    def test_zero_multiplier(self):
        self.assertEqual(multiply_int(5, 0), 0)

    def test_zero_multiplicand(self):
        self.assertEqual(multiply_int(0, 5), 0)

    def test_large_numbers(self):
        self.assertEqual(multiply_int(10000, 10000), 100000000)

    def test_one_as_multiplier(self):
        self.assertEqual(multiply_int(1, 9999), 9999)
        self.assertEqual(multiply_int(9999, 1), 9999)

    def test_negative_one(self):
        self.assertEqual(multiply_int(-1, 9999), -9999)
        self.assertEqual(multiply_int(9999, -1), -9999)

    def test_mixed_sign_combination(self):
        self.assertEqual(multiply_int(-10, 3), -30)
        self.assertEqual(multiply_int(10, -3), -30)

