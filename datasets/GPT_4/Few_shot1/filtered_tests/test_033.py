import unittest
from datasets.GPT_4.Few_shot1.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_surfacearea_sphere_zero(self): self.assertAlmostEqual(surfacearea_sphere(0), 0.0)

    def test_surfacearea_sphere_one(self): self.assertAlmostEqual(surfacearea_sphere(1), 4 * math.pi)

    def test_surfacearea_sphere_integer(self): self.assertAlmostEqual(surfacearea_sphere(3), 4 * math.pi * 9)

    def test_surfacearea_sphere_float(self): self.assertAlmostEqual(surfacearea_sphere(2.5), 4 * math.pi * 6.25)

    def test_surfacearea_sphere_large(self): self.assertAlmostEqual(surfacearea_sphere(1000), 4 * math.pi * 1000000)

    def test_surfacearea_sphere_negative(self): self.assertAlmostEqual(surfacearea_sphere(-2), 4 * math.pi * 4)

