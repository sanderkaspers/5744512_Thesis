import unittest
from datasets.o3.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(power(2, 3), 8)

    def test_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_zero_base_positive_exp(self):
        self.assertEqual(power(0, 5), 0)

    def test_negative_base_even_exp(self):
        self.assertEqual(power(-3, 2), 9)

    def test_negative_base_odd_exp(self):
        self.assertEqual(power(-2, 3), -8)

    def test_float_base(self):
        self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_one_base_any_exp(self):
        self.assertEqual(power(1, 999), 1)

