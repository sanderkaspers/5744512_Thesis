import unittest
from datasets.GPT_4.Zero_shot2.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_circ_1(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586)

    def test_circ_2(self):
        self.assertAlmostEqual(circle_circumference(0), 0.0)

    def test_circ_3(self):
        self.assertAlmostEqual(circle_circumference(-1), -6.283185307179586)

    def test_circ_4(self):
        self.assertAlmostEqual(circle_circumference(2.5), 15.707963267948966)

    def test_circ_5(self):
        self.assertAlmostEqual(circle_circumference(0.001), 0.006283185307179587)

    def test_circ_6(self):
        self.assertAlmostEqual(circle_circumference(100000), 628318.5307179586)

