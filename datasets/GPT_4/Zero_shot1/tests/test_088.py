import unittest
from datasets.GPT_4.Zero_shot1.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(area_polygon(4, 1), 1.0, places=5)

    def test_2(self):
        self.assertAlmostEqual(area_polygon(5, 1), 1.7204774, places=5)

    def test_3(self):
        self.assertAlmostEqual(area_polygon(1000, 1), 79577.4715, places=1)

    def test_4(self):
        self.assertAlmostEqual(area_polygon(6, 0.1), 0.0259807621, places=5)

    def test_5(self):
        self.assertAlmostEqual(area_polygon(6, 1000), 2.59807621e+5, places=1)

    def test_6(self):
        self.assertAlmostEqual(area_polygon(6, 2.5), 16.237975, places=5)

    def test_7(self):
        self.assertIsInstance(area_polygon(6, 2), float)

    def test_8(self):
        self.assertAlmostEqual(area_polygon(6, 1), 2.59807621, places=5)

