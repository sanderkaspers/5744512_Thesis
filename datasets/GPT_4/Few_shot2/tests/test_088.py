import unittest
from datasets.GPT_4.Few_shot2.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_area_polygon_square(self): self.assertAlmostEqual(area_polygon(4, 2), 4.0, places=2)

    def test_area_polygon_equilateral_triangle(self): self.assertAlmostEqual(area_polygon(3, 2), 1.73205, places=5)

    def test_area_polygon_regular_pentagon(self): self.assertAlmostEqual(area_polygon(5, 3), 15.4843, places=4)

    def test_area_polygon_large_sides(self): self.assertAlmostEqual(area_polygon(100, 1), 795.77, places=2)

    def test_area_polygon_minimal_valid(self): self.assertAlmostEqual(area_polygon(3, 1), 0.43301, places=5)

    def test_area_polygon_zero_length(self): self.assertEqual(area_polygon(5, 0), 0)

    def test_area_polygon_negative_length(self): self.assertLess(area_polygon(6, -2), 0)

    def test_area_polygon_non_integer_length(self): self.assertAlmostEqual(area_polygon(6, 2.5), 16.2372, places=4)

