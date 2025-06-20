import unittest
from datasets.GPT_4.Zero_shot1.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 4 * math.pi)

    def test_2(self):
        self.assertAlmostEqual(surfacearea_sphere(2), 4 * math.pi * 4)

    def test_3(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 4 * math.pi * 100)

    def test_4(self):
        self.assertAlmostEqual(surfacearea_sphere(0.5), 4 * math.pi * 0.25)

    def test_5(self):
        self.assertAlmostEqual(surfacearea_sphere(1000), 4 * math.pi * 1000000)

    def test_6(self):
        self.assertAlmostEqual(surfacearea_sphere(1e-3), 4 * math.pi * 1e-6)

    def test_7(self):
        self.assertAlmostEqual(surfacearea_sphere(math.pi), 4 * math.pi * (math.pi ** 2))

