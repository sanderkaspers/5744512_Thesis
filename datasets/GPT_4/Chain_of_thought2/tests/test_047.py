import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_zero(self): self.assertEqual(decimal_to_binary(0), '0')

    def test_positive_integer(self): self.assertEqual(decimal_to_binary(5), '101')

    def test_power_of_two(self): self.assertEqual(decimal_to_binary(8), '1000')

    def test_arbitrary_number(self): self.assertEqual(decimal_to_binary(42), '101010')

    def test_large_number(self): self.assertEqual(decimal_to_binary(1023), '1111111111')

    def test_negative_integer(self): self.assertEqual(decimal_to_binary(-5), '-101')

    def test_boolean_true(self): self.assertEqual(decimal_to_binary(True), '1')

    def test_boolean_false(self): self.assertEqual(decimal_to_binary(False), '0')

