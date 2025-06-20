import unittest
from datasets.GPT_4.Few_shot2.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_volume_sphere_radius_zero(self): self.assertAlmostEqual(volume_sphere(0), 0.0)

    def test_volume_sphere_radius_one(self): self.assertAlmostEqual(volume_sphere(1), (4/3) * math.pi)

    def test_volume_sphere_radius_two(self): self.assertAlmostEqual(volume_sphere(2), (4/3) * math.pi * 8)

    def test_volume_sphere_radius_pi(self): self.assertAlmostEqual(volume_sphere(math.pi), (4/3) * math.pi * math.pi**3)

    def test_volume_sphere_radius_fraction(self): self.assertAlmostEqual(volume_sphere(0.5), (4/3) * math.pi * (0.5)**3)

    def test_volume_sphere_negative_radius(self): self.assertAlmostEqual(volume_sphere(-1), -((4/3) * math.pi))

    def test_volume_sphere_large_radius(self): self.assertAlmostEqual(volume_sphere(1000), (4/3) * math.pi * 1000**3)

    def test_volume_sphere_small_radius(self): self.assertAlmostEqual(volume_sphere(1e-6), (4/3) * math.pi * (1e-6)**3)

