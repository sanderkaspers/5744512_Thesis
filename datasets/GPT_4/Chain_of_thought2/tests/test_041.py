import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer_exponent(self): self.assertEqual(power(2, 3), 8)

    def test_power_zero(self): self.assertEqual(power(5, 0), 1)

    def test_zero_base_positive_exponent(self): self.assertEqual(power(0, 5), 0)

    def test_exponent_one(self): self.assertEqual(power(3, 1), 3)

    def test_base_one(self): self.assertEqual(power(1, 100), 1)

    def test_zero_power_zero(self): self.assertEqual(power(0, 0), 1)

    def test_negative_base_odd_exponent(self): self.assertEqual(power(-2, 3), -8)

    def test_negative_base_even_exponent(self): self.assertEqual(power(-2, 4), 16)

