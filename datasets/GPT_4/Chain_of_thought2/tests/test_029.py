import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(power(2, 3), 8)

    def test_negative_base(self): self.assertEqual(power(-2, 3), -8)

    def test_negative_exponent(self): self.assertAlmostEqual(power(4, -2), 0.0625)

    def test_zero_base(self): self.assertEqual(power(0, 3), 0)

    def test_zero_power_zero(self): self.assertEqual(power(0, 0), 1)

    def test_float_inputs(self): self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_boolean_inputs(self): self.assertEqual(power(True, False), 1)

    def test_large_exponent(self): self.assertEqual(power(2, 20), 1048576)

    def test_complex_base(self): self.assertEqual(power(1 + 1j, 2), (1 + 1j) ** 2)

