import unittest
from datasets.GPT_4.Few_shot1.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_power_basic(self): self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self): self.assertEqual(power(5, 0), 1)

    def test_power_one_exponent(self): self.assertEqual(power(7, 1), 7)

    def test_power_zero_base(self): self.assertEqual(power(0, 5), 0)

    def test_power_zero_zero(self): self.assertEqual(power(0, 0), 1)

    def test_power_negative_base_even_exp(self): self.assertEqual(power(-2, 4), 16)

    def test_power_negative_base_odd_exp(self): self.assertEqual(power(-2, 3), -8)

    def test_power_large_exponent(self): self.assertEqual(power(2, 10), 1024)

    def test_power_one_base(self): self.assertEqual(power(1, 1000), 1)

