import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(decimal_to_binary(10), '1010')

    def test_zero_input(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_negative_integer(self):
        self.assertEqual(decimal_to_binary(-10), '-1010')

    def test_large_integer(self):
        self.assertEqual(decimal_to_binary(1024), '10000000000')

    def test_minimum_integer(self):
        self.assertEqual(decimal_to_binary(-2147483648), '-10000000000000000000000000000000')

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(10.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary('10')

    def test_single_bit_binary(self):
        self.assertEqual(decimal_to_binary(1), '1')

    def test_multiple_bit_binary(self):
        self.assertEqual(decimal_to_binary(7), '111')

