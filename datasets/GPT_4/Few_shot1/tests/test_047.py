import unittest
from datasets.GPT_4.Few_shot1.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_binary_zero(self): self.assertEqual(decimal_to_binary(0), '0')

    def test_binary_one(self): self.assertEqual(decimal_to_binary(1), '1')

    def test_binary_positive(self): self.assertEqual(decimal_to_binary(5), '101')

    def test_binary_large(self): self.assertEqual(decimal_to_binary(1023), '1111111111')

    def test_binary_even(self): self.assertEqual(decimal_to_binary(8), '1000')

    def test_binary_odd(self): self.assertEqual(decimal_to_binary(9), '1001')

    def test_binary_negative(self): self.assertEqual(decimal_to_binary(-3), bin(-3).replace("0b",""))

