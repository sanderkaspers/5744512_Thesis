import unittest
from datasets.mbpp.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_surfacearea_sphere_with_10_expect_1256_6370614359173(self):
        self.assertEqual(surfacearea_sphere(10), 1256.6370614359173)

    def test_surfacearea_sphere_with_15_expect_2827_4333882308138(self):
        self.assertEqual(surfacearea_sphere(15), 2827.4333882308138)

    def test_surfacearea_sphere_with_20_expect_5026_548245743669(self):
        self.assertEqual(surfacearea_sphere(20), 5026.548245743669)

