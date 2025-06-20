import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_radius_one(self): self.assertAlmostEqual(circle_circumference(1), 6.283, places=3)

    def test_radius_float(self): self.assertAlmostEqual(circle_circumference(2.5), 15.7075, places=4)

    def test_large_radius(self): self.assertAlmostEqual(circle_circumference(10000), 62830.0, places=1)

    def test_zero_radius(self): self.assertEqual(circle_circumference(0), 0.0)

    def test_small_radius(self): self.assertAlmostEqual(circle_circumference(1e-6), 6.283e-6, places=10)

    def test_negative_radius(self): self.assertAlmostEqual(circle_circumference(-2), -12.566, places=3)

    def test_boolean_input(self): self.assertAlmostEqual(circle_circumference(True), 6.283, places=3)

