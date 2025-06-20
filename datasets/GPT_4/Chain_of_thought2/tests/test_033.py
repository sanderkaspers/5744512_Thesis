import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer_radius(self): self.assertAlmostEqual(surfacearea_sphere(1), 4 * math.pi, places=5)

    def test_positive_float_radius(self): expected = 4 * math.pi * 2.5 * 2.5; self.assertAlmostEqual(surfacearea_sphere(2.5), expected, places=5)

    def test_large_radius(self): expected = 4 * math.pi * (1e6)**2; self.assertAlmostEqual(surfacearea_sphere(1e6), expected, places=2)

    def test_zero_radius(self): self.assertEqual(surfacearea_sphere(0), 0)

    def test_negative_radius(self): expected = 4 * math.pi * 9; self.assertAlmostEqual(surfacearea_sphere(-3), expected, places=5)

    def test_very_small_radius(self): expected = 4 * math.pi * (1e-9)**2; self.assertAlmostEqual(surfacearea_sphere(1e-9), expected, places=20)

    def test_boolean_true_input(self): self.assertAlmostEqual(surfacearea_sphere(True), 4 * math.pi, places=5)

