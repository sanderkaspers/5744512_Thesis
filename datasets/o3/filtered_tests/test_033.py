import unittest
from datasets.o3.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_surfacearea_zero(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_surfacearea_one(self):
        import math
        self.assertAlmostEqual(surfacearea_sphere(1), 4*math.pi)

    def test_surfacearea_float(self):
        import math
        self.assertAlmostEqual(surfacearea_sphere(2.5), 4*math.pi*2.5*2.5)

    def test_surfacearea_negative(self):
        import math
        self.assertAlmostEqual(surfacearea_sphere(-3), 4*math.pi*9)

    def test_surfacearea_non_numeric(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere("radius")

