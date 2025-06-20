import unittest
from datasets.o3.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_square_area(self):
        import math
        self.assertAlmostEqual(area_polygon(2, 4), 4.0, places=5)

    def test_triangle_area(self):
        import math
        expected = (3 * 3 ** 2) / (4 * math.tan(math.pi / 3))
        self.assertAlmostEqual(area_polygon(3, 3), expected, places=5)

    def test_pentagon_area(self):
        import math
        expected = (5 * 5 ** 2) / (4 * math.tan(math.pi / 5))
        self.assertAlmostEqual(area_polygon(5, 5), expected, places=5)

    def test_zero_sides_raises(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(2, 0)

    def test_negative_side_length(self):
        import math
        self.assertAlmostEqual(area_polygon(-4, 4), 16.0, places=5)

    def test_large_n_approaches_circle(self):
        # A 1000‑gon with side length 1 approximates area ~785
        area = area_polygon(1, 1000)
        self.assertTrue(780 < area < 790)

