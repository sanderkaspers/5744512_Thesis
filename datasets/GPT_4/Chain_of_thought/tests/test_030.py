import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_sphere(3), 113.09733552923255)

    def test_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0.0)

    def test_negative_radius(self):
        self.assertAlmostEqual(volume_sphere(-3), -113.09733552923255)

    def test_floating_point_radius(self):
        self.assertAlmostEqual(volume_sphere(2.5), 65.44984694978735)

    def test_large_radius(self):
        self.assertAlmostEqual(volume_sphere(1000), 4188790204.7863903)

    def test_small_radius(self):
        self.assertAlmostEqual(volume_sphere(0.001), 4.1887902047863905e-09)

    def test_max_float(self):
        self.assertTrue(volume_sphere(1.7976931348623157e+308) > 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            volume_sphere('10')

