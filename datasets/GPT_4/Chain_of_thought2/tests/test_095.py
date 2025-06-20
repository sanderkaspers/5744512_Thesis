import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(perimeter_pentagon(5), 25)

    def test_positive_float(self): self.assertAlmostEqual(perimeter_pentagon(3.2), 16.0)

    def test_zero_side_length(self): self.assertEqual(perimeter_pentagon(0), 0)

    def test_negative_side(self): self.assertEqual(perimeter_pentagon(-4), -20)

    def test_very_large_number(self): self.assertEqual(perimeter_pentagon(1e6), 5e6)

    def test_very_small_number(self): self.assertAlmostEqual(perimeter_pentagon(1e-6), 5e-6)

    def test_boolean_input(self): self.assertEqual(perimeter_pentagon(True), 5); self.assertEqual(perimeter_pentagon(False), 0)

    def test_complex_input(self): self.assertEqual(perimeter_pentagon(2+3j), 10+15j)

