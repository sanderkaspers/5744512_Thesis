import unittest
from datasets.o3.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_zero_angle(self):
        import math
        self.assertTrue(math.isclose(angle_complex(1,0), 0.0, rel_tol=1e-9))

    def test_positive_imag(self):
        import math
        self.assertTrue(math.isclose(angle_complex(0,1), math.pi/2, rel_tol=1e-9))

    def test_negative_real(self):
        import math
        result = angle_complex(-1,0)
        # phase for (-1+0j) should be pi
        self.assertTrue(math.isclose(abs(result), math.pi, rel_tol=1e-9))

    def test_negative_imag(self):
        import math
        self.assertTrue(math.isclose(angle_complex(0,-1), -math.pi/2, rel_tol=1e-9))

    def test_quadrant_two(self):
        import math
        expected = 3*math.pi/4
        self.assertTrue(math.isclose(angle_complex(-1,1), expected, rel_tol=1e-9))

