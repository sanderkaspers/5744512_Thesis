import unittest
from datasets.GPT_4.Zero_shot2.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(surfacearea_sphere(0), 0.0)

    def test_area_2(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 4 * math.pi)

    def test_area_3(self):
        self.assertAlmostEqual(surfacearea_sphere(2), 16 * math.pi)

    def test_area_4(self):
        self.assertAlmostEqual(surfacearea_sphere(-1), 4 * math.pi)

    def test_area_5(self):
        self.assertAlmostEqual(surfacearea_sphere(1e6), 4 * math.pi * 1e12)

    def test_area_6(self):
        self.assertAlmostEqual(surfacearea_sphere(1e-10), 4 * math.pi * 1e-20)

    def test_area_7(self):
        self.assertAlmostEqual(surfacearea_sphere(2.5), 4 * math.pi * 6.25)

