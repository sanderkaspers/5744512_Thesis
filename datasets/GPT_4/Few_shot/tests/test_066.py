import unittest
from datasets.GPT_4.Few_shot.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(angle_complex(1, 1), cmath.pi / 4) # Angle 45 degrees)

    def test_case_2(self):
        self.assertEqual(angle_complex(-1, -1), -3 * cmath.pi / 4) # Angle -135 degrees)

    def test_case_3(self):
        self.assertEqual(angle_complex(1, 0), 0) # Real axis, 0 degrees)

    def test_case_4(self):
        self.assertEqual(angle_complex(0, 1), cmath.pi / 2) # Imaginary axis, 90 degrees)

    def test_case_5(self):
        self.assertEqual(angle_complex(-1, 0), cmath.pi) # Negative real axis, 180 degrees)

    def test_case_6(self):
        self.assertEqual(angle_complex(0, -1), -cmath.pi / 2) # Negative imaginary axis, -90 degrees)

    def test_case_7(self):
        self.assertEqual(angle_complex(0, 0), 0) # Origin, undefined but returns 0)

    def test_case_8(self):
        self.assertEqual(angle_complex(3, 4), cmath.phase(complex(3, 4)) )  # General complex number)

