import unittest
from datasets.GPT_4.Few_shot1.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_perimeter_pentagon_integer(self): self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_pentagon_zero(self): self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_pentagon_one(self): self.assertEqual(perimeter_pentagon(1), 5)

    def test_perimeter_pentagon_float(self): self.assertEqual(perimeter_pentagon(2.5), 12.5)

    def test_perimeter_pentagon_large_value(self): self.assertEqual(perimeter_pentagon(1000000), 5000000)

    def test_perimeter_pentagon_negative(self): self.assertEqual(perimeter_pentagon(-3), -15)

    def test_perimeter_pentagon_small_float(self): self.assertEqual(perimeter_pentagon(0.1), 0.5)

    def test_perimeter_pentagon_scientific(self): self.assertEqual(perimeter_pentagon(1e2), 500.0)

    def test_perimeter_pentagon_boolean_true(self): self.assertEqual(perimeter_pentagon(True), 5)

    def test_perimeter_pentagon_boolean_false(self): self.assertEqual(perimeter_pentagon(False), 0)

    def test_perimeter_pentagon_extreme_negative(self): self.assertEqual(perimeter_pentagon(-1e6), -5e6)

    def test_perimeter_pentagon_large_float(self): self.assertEqual(perimeter_pentagon(1.23456789), 6.17283945)

