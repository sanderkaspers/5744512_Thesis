import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_zero_celsius(self): self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_hundred_celsius(self): self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative_symmetric(self): self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_positive_float(self): self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=2)

    def test_negative_float(self): self.assertAlmostEqual(celsius_to_fahrenheit(-12.5), 9.5, places=2)

    def test_large_value(self): self.assertEqual(celsius_to_fahrenheit(1e6), (1e6 * 9/5) + 32)

    def test_small_value(self): self.assertAlmostEqual(celsius_to_fahrenheit(1e-6), 32.0000018, places=7)

    def test_boolean_true(self): self.assertEqual(celsius_to_fahrenheit(True), (1 * 9/5) + 32)

    def test_boolean_false(self): self.assertEqual(celsius_to_fahrenheit(False), 32.0)

    def test_scientific_notation(self): self.assertEqual(celsius_to_fahrenheit(5e1), (50 * 9/5) + 32)

