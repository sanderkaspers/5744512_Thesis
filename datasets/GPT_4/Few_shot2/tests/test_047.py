import unittest
from datasets.GPT_4.Few_shot2.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_decimal_to_binary_zero(self): self.assertEqual(decimal_to_binary(0), '0b0')

    def test_decimal_to_binary_one(self): self.assertEqual(decimal_to_binary(1), '0b1')

    def test_decimal_to_binary_positive(self): self.assertEqual(decimal_to_binary(10), '0b1010')

    def test_decimal_to_binary_large_number(self): self.assertEqual(decimal_to_binary(255), '0b11111111')

    def test_decimal_to_binary_negative(self): self.assertEqual(decimal_to_binary(-5), '-0b101')

    def test_decimal_to_binary_power_of_two(self): self.assertEqual(decimal_to_binary(8), '0b1000')

