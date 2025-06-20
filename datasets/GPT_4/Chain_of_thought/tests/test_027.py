import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_typical_case_divisible(self):
        self.assertTrue(is_Diff(22))  # 22 is divisible by 11

    def test_not_divisible(self):
        self.assertFalse(is_Diff(23))  # 23 is not divisible by 11

    def test_zero(self):
        self.assertTrue(is_Diff(0))  # 0 is divisible by any number

    def test_negative_divisible(self):
        self.assertTrue(is_Diff(-33))  # -33 is divisible by 11

    def test_negative_not_divisible(self):
        self.assertFalse(is_Diff(-25))  # -25 is not divisible by 11

    def test_large_number_divisible(self):
        self.assertTrue(is_Diff(110000000000000011))  # Large number divisible by 11

    def test_large_number_not_divisible(self):
        self.assertFalse(is_Diff(110000000000000013))  # Large number not divisible by 11

    def test_floating_point_number(self):
        with self.assertRaises(TypeError):
            is_Diff(22.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            is_Diff('22')

    def test_max_integer(self):
        self.assertTrue(is_Diff(9223372036854775807 % 11 == 0))

