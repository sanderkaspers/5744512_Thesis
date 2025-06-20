import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(divide(10, 2), 5.0)

    def test_int_float(self): self.assertEqual(divide(9, 2.0), 4.5)

    def test_float_int(self): self.assertEqual(divide(9.0, 2), 4.5)

    def test_float_float(self): self.assertEqual(divide(7.5, 2.5), 3.0)

    def test_negative_division(self): self.assertEqual(divide(-10, 2), -5.0)

    def test_zero_numerator(self): self.assertEqual(divide(0, 5), 0.0)

    def test_boolean_division(self): self.assertEqual(divide(True, True), 1.0)

    def test_scientific_notation(self): self.assertEqual(divide(1e4, 1e2), 100.0)

    def test_complex_division(self): self.assertEqual(divide(4 + 2j, 1 + 1j), (4 + 2j) / (1 + 1j))

