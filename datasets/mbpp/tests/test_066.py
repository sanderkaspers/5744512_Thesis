import unittest
from datasets.mbpp.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_angle_complex_with_0_1j_expect_1_5707963267948966(self):
        self.assertEqual(angle_complex(0,1j), 1.5707963267948966)

    def test_angle_complex_with_2_1j_expect_0_4636476090008061(self):
        self.assertEqual(angle_complex(2,1j), 0.4636476090008061)

    def test_angle_complex_with_0_2j_expect_1_5707963267948966(self):
        self.assertEqual(angle_complex(0,2j), 1.5707963267948966)

