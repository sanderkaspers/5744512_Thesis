import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_angle_positive_real(self): self.assertAlmostEqual(angle_complex(1, 0), 0.0)

    def test_angle_negative_real(self): self.assertAlmostEqual(angle_complex(-1, 0), math.pi)

    def test_angle_positive_imaginary(self): self.assertAlmostEqual(angle_complex(0, 1), math.pi / 2)

    def test_angle_negative_imaginary(self): self.assertAlmostEqual(angle_complex(0, -1), -math.pi / 2)

    def test_angle_first_quadrant(self): self.assertAlmostEqual(angle_complex(1, 1), math.pi / 4)

    def test_angle_second_quadrant(self): self.assertAlmostEqual(angle_complex(-1, 1), 3 * math.pi / 4)

    def test_angle_third_quadrant(self): self.assertAlmostEqual(angle_complex(-1, -1), -3 * math.pi / 4)

    def test_angle_fourth_quadrant(self): self.assertAlmostEqual(angle_complex(1, -1), -math.pi / 4)

    def test_angle_origin(self): self.assertAlmostEqual(angle_complex(0, 0), 0.0)

    def test_large_values(self): self.assertAlmostEqual(angle_complex(1e6, 1e6), math.pi / 4)

    def test_small_values(self): self.assertAlmostEqual(angle_complex(1e-6, 1e-6), math.pi / 4)

    def test_float_inputs(self): self.assertAlmostEqual(angle_complex(0.0, -3.0), -math.pi / 2)

