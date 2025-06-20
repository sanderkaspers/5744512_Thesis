import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(cube(3), 27)

    def test_negative_integer(self): self.assertEqual(cube(-2), -8)

    def test_zero(self): self.assertEqual(cube(0), 0)

    def test_positive_float(self): self.assertEqual(cube(1.5), 3.375)

    def test_negative_float(self): self.assertEqual(cube(-2.0), -8.0)

    def test_large_number(self): self.assertEqual(cube(1e4), 1e12)

    def test_small_float(self): self.assertAlmostEqual(cube(1e-3), 1e-9)

    def test_boolean_true(self): self.assertEqual(cube(True), 1)

    def test_boolean_false(self): self.assertEqual(cube(False), 0)

    def test_scientific_notation(self): self.assertEqual(cube(1e2), 1e6)

    def test_complex_number(self): self.assertEqual(cube(1 + 1j), (1 + 1j)**3)

