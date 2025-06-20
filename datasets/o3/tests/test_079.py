import unittest
from datasets.o3.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_unit_radius(self):
        self.assertAlmostEqual(circle_circumference(1), 2*3.1415*1, places=4)

    def test_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_large_radius(self):
        self.assertAlmostEqual(circle_circumference(1000), 2*3.1415*1000, places=2)

    def test_float_radius(self):
        self.assertAlmostEqual(circle_circumference(2.5), 2*3.1415*2.5, places=4)

    def test_negative_radius(self):
        self.assertAlmostEqual(circle_circumference(-3), -2*3.1415*3, places=4)

    def test_precision(self):
        # Compare with math.tau for higher precision reference
        expected = math.tau/2*3  # tau = 2π, but function uses 3.1415 approximation
        self.assertAlmostEqual(circle_circumference(1.5), 2*3.1415*1.5, places=4)

