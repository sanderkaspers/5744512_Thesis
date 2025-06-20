import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_sphere(3), 113.09733552923255)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_sphere(0), 0.0)

    def test_negative_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(-3), 113.09733552923255)

    def test_floating_point_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(2.5), 78.53981633974483)

    def test_large_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(1000), 12566370.614359172)

    def test_small_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(0.001), 1.2566370614359173e-05)

    def test_max_float(self):
        self.assertTrue(surfacearea_sphere(1.7976931348623157e+308) > 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('10')

