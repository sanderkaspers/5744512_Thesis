import unittest
from datasets.GPT_4.Few_shot2.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_perimeter_pentagon_positive_integer(self): self.assertEqual(perimeter_pentagon(3), 15)

    def test_perimeter_pentagon_zero(self): self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_pentagon_positive_float(self): self.assertAlmostEqual(perimeter_pentagon(2.5), 12.5)

    def test_perimeter_pentagon_large_number(self): self.assertEqual(perimeter_pentagon(1000), 5000)

    def test_perimeter_pentagon_negative_input(self): self.assertEqual(perimeter_pentagon(-2), -10)

    def test_perimeter_pentagon_small_decimal(self): self.assertAlmostEqual(perimeter_pentagon(0.2), 1.0)

