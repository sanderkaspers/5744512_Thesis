import unittest
from datasets.GPT_4.Few_shot2.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_surfacearea_sphere_radius_zero(self): self.assertAlmostEqual(surfacearea_sphere(0), 0.0)

    def test_surfacearea_sphere_radius_one(self): self.assertAlmostEqual(surfacearea_sphere(1), 4 * math.pi)

    def test_surfacearea_sphere_radius_two(self): self.assertAlmostEqual(surfacearea_sphere(2), 4 * math.pi * 4)

    def test_surfacearea_sphere_radius_pi(self): self.assertAlmostEqual(surfacearea_sphere(math.pi), 4 * math.pi * math.pi**2)

    def test_surfacearea_sphere_radius_half(self): self.assertAlmostEqual(surfacearea_sphere(0.5), 4 * math.pi * (0.5)**2)

    def test_surfacearea_sphere_negative_radius(self): self.assertAlmostEqual(surfacearea_sphere(-1), 4 * math.pi)

    def test_surfacearea_sphere_large_radius(self): self.assertAlmostEqual(surfacearea_sphere(1000), 4 * math.pi * 1000000)

    def test_surfacearea_sphere_small_radius(self): self.assertAlmostEqual(surfacearea_sphere(1e-6), 4 * math.pi * (1e-6)**2)

