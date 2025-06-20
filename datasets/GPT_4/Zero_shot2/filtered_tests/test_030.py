import unittest
from datasets.GPT_4.Zero_shot2.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_sphere_1(self):
        self.assertEqual(volume_sphere(0), 0.0)

    def test_sphere_2(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3)*math.pi)

    def test_sphere_3(self):
        self.assertAlmostEqual(volume_sphere(2), (4/3)*math.pi*8)

    def test_sphere_4(self):
        self.assertAlmostEqual(volume_sphere(-1), -(4/3)*math.pi)

    def test_sphere_5(self):
        self.assertAlmostEqual(volume_sphere(1e6), (4/3)*math.pi*1e18)

    def test_sphere_6(self):
        self.assertAlmostEqual(volume_sphere(1e-10), (4/3)*math.pi*1e-30)

    def test_sphere_7(self):
        self.assertAlmostEqual(volume_sphere(2.5), (4/3)*math.pi*15.625)

