import unittest
from datasets.GPT_4.Few_shot1.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_angle_positive_real(self): self.assertAlmostEqual(angle_complex(1, 0), 0.0)

    def test_angle_positive_imag(self): self.assertAlmostEqual(angle_complex(0, 1), 1.57079632679)

    def test_angle_negative_real(self): self.assertAlmostEqual(angle_complex(-1, 0), 3.14159265359)

    def test_angle_negative_imag(self): self.assertAlmostEqual(angle_complex(0, -1), -1.57079632679)

    def test_angle_quadrant_I(self): self.assertAlmostEqual(angle_complex(1, 1), 0.78539816339)

    def test_angle_quadrant_II(self): self.assertAlmostEqual(angle_complex(-1, 1), 2.35619449019)

    def test_angle_quadrant_III(self): self.assertAlmostEqual(angle_complex(-1, -1), -2.35619449019)

    def test_angle_quadrant_IV(self): self.assertAlmostEqual(angle_complex(1, -1), -0.78539816339)

    def test_angle_zero_zero(self): self.assertAlmostEqual(angle_complex(0, 0), 0.0)

    def test_angle_large_values(self): self.assertAlmostEqual(angle_complex(1000, 1000), 0.78539816339)

