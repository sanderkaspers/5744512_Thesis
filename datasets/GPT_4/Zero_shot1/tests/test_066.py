import unittest
from datasets.GPT_4.Zero_shot1.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_2(self):
        self.assertEqual(angle_complex(2, 0), 0.0)

    def test_3(self):
        self.assertAlmostEqual(angle_complex(0, 2), 1.5707963267948966)

    def test_4(self):
        self.assertAlmostEqual(angle_complex(-1, -1), -2.356194490192345)

    def test_5(self):
        self.assertEqual(angle_complex(0, 0), 0.0)

    def test_6(self):
        self.assertIsInstance(angle_complex(1, 0), float)

