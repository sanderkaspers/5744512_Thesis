import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_positive_int(self): self.assertEqual(decimal_to_binary(5), '0b101')

    def test_zero(self): self.assertEqual(decimal_to_binary(0), '0b0')

    def test_negative_int(self): self.assertEqual(decimal_to_binary(-3), '-0b11')

    def test_large_int(self): self.assertEqual(decimal_to_binary(1023), '0b1111111111')

    def test_bool_input(self): self.assertEqual(decimal_to_binary(True), '0b1'); self.assertEqual(decimal_to_binary(False), '0b0')

