import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(circle_circumference(5), 31.415)

    def test_small_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(0.1), 0.6283)

    def test_large_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(10000), 62830)

    def test_zero_radius(self):
        self.assertAlmostEqual(circle_circumference(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_circumference(-5)

    def test_floating_point_radius(self):
        self.assertAlmostEqual(circle_circumference(2.5), 15.7075)

    def test_very_small_floating_point_radius(self):
        self.assertAlmostEqual(circle_circumference(1e-10), 6.283e-10)

    def test_very_large_floating_point_radius(self):
        self.assertAlmostEqual(circle_circumference(1e10), 6.283e10)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            circle_circumference('10')

    def test_radius_none(self):
        with self.assertRaises(TypeError):
            circle_circumference(None)

