import unittest
from datasets.GPT_4.Few_shot2.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_angle_complex_zero(self): self.assertEqual(angle_complex(0, 0), 0.0)

    def test_angle_complex_positive_real(self): self.assertEqual(angle_complex(1, 0), 0.0)

    def test_angle_complex_negative_real(self): self.assertEqual(angle_complex(-1, 0), math.pi)

    def test_angle_complex_positive_imaginary(self): self.assertEqual(angle_complex(0, 1), math.pi/2)

    def test_angle_complex_negative_imaginary(self): self.assertEqual(angle_complex(0, -1), -math.pi/2)

    def test_angle_complex_first_quadrant(self): self.assertAlmostEqual(angle_complex(1, 1), math.pi/4, places=6)

    def test_angle_complex_second_quadrant(self): self.assertAlmostEqual(angle_complex(-1, 1), 3*math.pi/4, places=6)

    def test_angle_complex_third_quadrant(self): self.assertAlmostEqual(angle_complex(-1, -1), -3*math.pi/4, places=6)

    def test_angle_complex_fourth_quadrant(self): self.assertAlmostEqual(angle_complex(1, -1), -math.pi/4, places=6)

