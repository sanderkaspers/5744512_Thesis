import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_positive_real(self): self.assertAlmostEqual(angle_complex(1, 0), 0.0)

    def test_positive_imaginary(self): self.assertAlmostEqual(angle_complex(0, 1), math.pi / 2)

    def test_negative_imaginary(self): self.assertAlmostEqual(angle_complex(0, -1), -math.pi / 2)

    def test_negative_real(self): self.assertAlmostEqual(angle_complex(-1, 0), math.pi)

    def test_pi_over_4(self): self.assertAlmostEqual(angle_complex(1, 1), math.pi / 4)

    def test_3pi_over_4(self): self.assertAlmostEqual(angle_complex(-1, 1), 3 * math.pi / 4)

    def test_negative_3pi_over_4(self): self.assertAlmostEqual(angle_complex(-1, -1), -3 * math.pi / 4)

    def test_negative_pi_over_4(self): self.assertAlmostEqual(angle_complex(1, -1), -math.pi / 4)

    def test_zero_vector(self): self.assertAlmostEqual(angle_complex(0, 0), 0.0)

    def test_float_inputs(self): self.assertAlmostEqual(angle_complex(0.0, 1.0), math.pi / 2)

