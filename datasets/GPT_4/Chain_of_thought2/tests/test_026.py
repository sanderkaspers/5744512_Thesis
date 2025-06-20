import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_integer_remainder(self): self.assertEqual(remainder(10, 3), 1)

    def test_negative_dividend(self): self.assertEqual(remainder(-10, 3), 2)

    def test_negative_divisor(self): self.assertEqual(remainder(10, -3), -2)

    def test_both_negative(self): self.assertEqual(remainder(-10, -3), -1)

    def test_float_inputs(self): self.assertAlmostEqual(remainder(7.5, 2.5), 0.0)

    def test_zero_dividend(self): self.assertEqual(remainder(0, 3), 0)

    def test_boolean_values(self): self.assertEqual(remainder(True, True), 0)

