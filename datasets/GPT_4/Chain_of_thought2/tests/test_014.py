import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_freezing_point(self): self.assertEqual(fahrenheit_to_celsius(32), 0.0)

    def test_boiling_point(self): self.assertEqual(fahrenheit_to_celsius(212), 100.0)

    def test_negative_symmetric(self): self.assertEqual(fahrenheit_to_celsius(-40), -40.0)

    def test_float_input(self): self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=1)

    def test_negative_float(self): self.assertAlmostEqual(fahrenheit_to_celsius(-10.5), -23.6111, places=4)

    def test_large_value(self): self.assertEqual(fahrenheit_to_celsius(1e6), (1e6 - 32) * 5/9)

    def test_small_value(self): self.assertAlmostEqual(fahrenheit_to_celsius(1e-6), (1e-6 - 32) * 5/9, places=7)

    def test_boolean_true(self): self.assertEqual(fahrenheit_to_celsius(True), (1 - 32) * 5/9)

    def test_boolean_false(self): self.assertEqual(fahrenheit_to_celsius(False), (0 - 32) * 5/9)

    def test_scientific_notation(self): self.assertEqual(fahrenheit_to_celsius(1e2), (100 - 32) * 5/9)

