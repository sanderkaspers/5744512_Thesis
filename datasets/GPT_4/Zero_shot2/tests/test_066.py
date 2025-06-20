import unittest
from datasets.GPT_4.Zero_shot2.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_angle_1(self):
        self.assertAlmostEqual(angle_complex(1, 0), 0)

    def test_angle_2(self):
        self.assertAlmostEqual(angle_complex(-1, 0), cmath.pi)

    def test_angle_3(self):
        self.assertAlmostEqual(angle_complex(0, 1), cmath.pi/2)

    def test_angle_4(self):
        self.assertAlmostEqual(angle_complex(0, -1), -cmath.pi/2)

    def test_angle_5(self):
        self.assertAlmostEqual(angle_complex(1, 1), cmath.pi/4)

    def test_angle_6(self):
        self.assertAlmostEqual(angle_complex(-1, 1), 3*cmath.pi/4)

    def test_angle_7(self):
        self.assertAlmostEqual(angle_complex(-1, -1), -3*cmath.pi/4)

    def test_angle_8(self):
        self.assertAlmostEqual(angle_complex(1, -1), -cmath.pi/4)

    def test_angle_9(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)

