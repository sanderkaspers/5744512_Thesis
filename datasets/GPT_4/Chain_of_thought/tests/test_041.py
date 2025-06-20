import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(power(2, 3), 8)

    def test_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_zero_base(self):
        self.assertEqual(power(0, 3), 0)

    def test_exponent_one(self):
        self.assertEqual(power(7, 1), 7)

    def test_negative_exponent(self):
        self.assertEqual(power(2, -2), None)

    def test_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_fractional_base(self):
        self.assertEqual(power(0.5, 2), 0.25)

    def test_large_exponent(self):
        self.assertEqual(power(2, 20), 1048576)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            power('2', 3)

    def test_boundary_values(self):
        self.assertEqual(power(2147483647, 1), 2147483647)
        self.assertEqual(power(1, 2147483647), 1)

