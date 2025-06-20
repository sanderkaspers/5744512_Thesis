import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(divisor(12), 6)

    def test_prime_number(self):
        self.assertEqual(divisor(13), 2)

    def test_one_input(self):
        self.assertEqual(divisor(1), 1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            divisor(0)

    def test_negative_integer(self):
        self.assertEqual(divisor(-12), 6)

    def test_large_integer(self):
        self.assertEqual(divisor(10000), 25)

    def test_min_integer(self):
        with self.assertRaises(ValueError):
            divisor(-2147483648)

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            divisor(12.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            divisor('twelve')

