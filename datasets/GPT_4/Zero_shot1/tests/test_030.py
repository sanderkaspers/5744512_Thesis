import unittest
from datasets.GPT_4.Zero_shot1.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3) * math.pi)

    def test_2(self):
        self.assertAlmostEqual(volume_sphere(2), (4/3) * math.pi * 8)

    def test_3(self):
        self.assertAlmostEqual(volume_sphere(10), (4/3) * math.pi * 1000)

    def test_4(self):
        self.assertAlmostEqual(volume_sphere(0.5), (4/3) * math.pi * (0.5 ** 3))

    def test_5(self):
        self.assertAlmostEqual(volume_sphere(math.pi), (4/3) * math.pi * (math.pi ** 3))

    def test_6(self):
        self.assertAlmostEqual(volume_sphere(1e-5), (4/3) * math.pi * (1e-5)**3)

    def test_7(self):
        self.assertAlmostEqual(volume_sphere(1e5), (4/3) * math.pi * (1e5)**3)

