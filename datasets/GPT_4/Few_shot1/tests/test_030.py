import unittest
from datasets.GPT_4.Few_shot1.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_volume_sphere_zero_radius(self): self.assertAlmostEqual(volume_sphere(0), 0.0)

    def test_volume_sphere_unit_radius(self): self.assertAlmostEqual(volume_sphere(1), (4.0 / 3.0) * math.pi)

    def test_volume_sphere_integer_radius(self): self.assertAlmostEqual(volume_sphere(3), (4.0 / 3.0) * math.pi * 27)

    def test_volume_sphere_float_radius(self): self.assertAlmostEqual(volume_sphere(2.5), (4.0 / 3.0) * math.pi * math.pow(2.5, 3))

    def test_volume_sphere_large_radius(self): self.assertAlmostEqual(volume_sphere(1000), (4.0 / 3.0) * math.pi * 1000000000)

    def test_volume_sphere_negative_radius(self): self.assertAlmostEqual(volume_sphere(-1), -(4.0 / 3.0) * math.pi)

    def test_volume_sphere_precision_check(self): self.assertAlmostEqual(volume_sphere(2), (4.0 / 3.0) * math.pi * 8)

    def test_volume_sphere_extreme_precision(self): self.assertAlmostEqual(volume_sphere(1e-10), (4.0 / 3.0) * math.pi * math.pow(1e-10, 3))

    def test_volume_sphere_very_large_float(self): self.assertAlmostEqual(volume_sphere(1e+5), (4.0 / 3.0) * math.pi * math.pow(1e+5, 3))

