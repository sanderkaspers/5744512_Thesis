import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 1), cmath.phase(complex(1, 1)))

    def test_real_part_zero(self):
        self.assertAlmostEqual(angle_complex(0, 1), cmath.phase(complex(0, 1)))

    def test_imaginary_part_zero(self):
        self.assertAlmostEqual(angle_complex(1, 0), cmath.phase(complex(1, 0)))

    def test_both_parts_zero(self):
        self.assertAlmostEqual(angle_complex(0, 0), cmath.phase(complex(0, 0)))

    def test_negative_real_part(self):
        self.assertAlmostEqual(angle_complex(-1, 1), cmath.phase(complex(-1, 1)))

    def test_negative_imaginary_part(self):
        self.assertAlmostEqual(angle_complex(1, -1), cmath.phase(complex(1, -1)))

    def test_both_parts_negative(self):
        self.assertAlmostEqual(angle_complex(-1, -1), cmath.phase(complex(-1, -1)))

    def test_on_axes(self):
        self.assertAlmostEqual(angle_complex(1, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1), cmath.pi / 2)
        self.assertAlmostEqual(angle_complex(-1, 0), cmath.pi)
        self.assertAlmostEqual(angle_complex(0, -1), -cmath.pi / 2)

    def test_very_large_values(self):
        self.assertAlmostEqual(angle_complex(1e10, 1e10), cmath.phase(complex(1e10, 1e10)))

    def test_floating_point_precision(self):
        self.assertAlmostEqual(angle_complex(1e-10, 1e-10), cmath.phase(complex(1e-10, 1e-10)))

