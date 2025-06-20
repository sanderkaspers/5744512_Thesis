import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_zero(self): self.assertEqual(surfacearea_sphere(0), 0.0)

    def test_radius_one(self): self.assertAlmostEqual(surfacearea_sphere(1), 4 * math.pi, places=6)

    def test_radius_two(self): self.assertAlmostEqual(surfacearea_sphere(2), 4 * math.pi * 4, places=6)

    def test_large_radius(self): self.assertAlmostEqual(surfacearea_sphere(1000), 4 * math.pi * 1000000, places=2)

    def test_float_radius(self): self.assertAlmostEqual(surfacearea_sphere(1.5), 4 * math.pi * (1.5**2), places=6)

    def test_negative_radius(self): self.assertAlmostEqual(surfacearea_sphere(-2), 4 * math.pi * 4, places=6)

