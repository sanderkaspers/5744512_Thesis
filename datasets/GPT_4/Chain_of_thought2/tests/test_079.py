import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_radius_integer(self): self.assertAlmostEqual(circle_circumference(1), 6.283)

    def test_radius_float(self): self.assertAlmostEqual(circle_circumference(2.5), 15.7075)

    def test_radius_zero(self): self.assertEqual(circle_circumference(0), 0.0)

    def test_radius_negative(self): self.assertAlmostEqual(circle_circumference(-3), -18.849)

    def test_large_radius(self): self.assertAlmostEqual(circle_circumference(1_000_000), 6283000.0)

    def test_small_radius(self): self.assertAlmostEqual(circle_circumference(1e-6), 6.283e-6)

    def test_complex_input(self): self.assertEqual(circle_circumference(complex(2, 0)), 6.283 * complex(2, 0))

