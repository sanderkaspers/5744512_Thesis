import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(area_triangle(10, 5), 25.0)

    def test_positive_floats(self): self.assertEqual(area_triangle(2.5, 4.0), 5.0)

    def test_zero_base(self): self.assertEqual(area_triangle(0, 5), 0.0)

    def test_zero_height(self): self.assertEqual(area_triangle(5, 0), 0.0)

    def test_zero_base_and_height(self): self.assertEqual(area_triangle(0, 0), 0.0)

    def test_negative_base(self): self.assertEqual(area_triangle(-3, 4), -6.0)

    def test_negative_height(self): self.assertEqual(area_triangle(3, -4), -6.0)

    def test_both_negative(self): self.assertEqual(area_triangle(-3, -4), 6.0)

    def test_large_values(self): self.assertEqual(area_triangle(1e6, 2e6), 1e12)

    def test_small_values(self): self.assertAlmostEqual(area_triangle(1e-6, 2e-6), 1e-12)

    def test_mixed_types(self): self.assertEqual(area_triangle(5, 2.5), 6.25)

    def test_scientific_notation(self): self.assertEqual(area_triangle(5e2, 2e1), 5000.0)

    def test_boolean_inputs(self): self.assertEqual(area_triangle(True, False), 0.0)

