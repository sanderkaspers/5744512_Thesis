import unittest
from datasets.o3.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_unit_sphere(self):
        import math
        self.assertTrue(math.isclose(volume_sphere(1), (4/3)*math.pi))

    def test_radius_three(self):
        import math
        self.assertTrue(math.isclose(volume_sphere(3), 36*math.pi))

    def test_negative_radius(self):
        import math
        self.assertTrue(math.isclose(volume_sphere(-2), -(32/3)*math.pi))

    def test_float_radius(self):
        import math
        self.assertTrue(math.isclose(volume_sphere(2.5), (4/3)*math.pi*15.625))

