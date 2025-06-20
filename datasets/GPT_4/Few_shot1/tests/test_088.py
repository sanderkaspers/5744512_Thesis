import unittest
from datasets.GPT_4.Few_shot1.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_area_polygon_triangle(self): self.assertAlmostEqual(area_polygon(3, 1), 0.43301270189221946)

    def test_area_polygon_square(self): self.assertAlmostEqual(area_polygon(4, 2), 4.0)

    def test_area_polygon_pentagon(self): self.assertAlmostEqual(area_polygon(5, 3), 15.484296605300704)

    def test_area_polygon_hexagon(self): self.assertAlmostEqual(area_polygon(6, 2), 10.392304845413264)

    def test_area_polygon_decagon(self): self.assertAlmostEqual(area_polygon(10, 1), 7.694208842938132)

    def test_area_polygon_large_sides(self): self.assertAlmostEqual(area_polygon(1000, 1), 79577.47154594767)

    def test_area_polygon_small_side_length(self): self.assertAlmostEqual(area_polygon(6, 0.1), 0.04332305964663776)

    def test_area_polygon_large_side_length(self): self.assertAlmostEqual(area_polygon(4, 1000), 1000000.0)

    def test_area_polygon_float_inputs(self): self.assertAlmostEqual(area_polygon(5.0, 3.0), 15.484296605300704)

    def test_area_polygon_invalid_side_length_zero(self): self.assertEqual(area_polygon(6, 0), 0.0)

    def test_area_polygon_invalid_side_length_negative(self): self.assertLess(area_polygon(6, -1), 0.0)

    def test_area_polygon_extremely_large(self): self.assertAlmostEqual(area_polygon(1000000, 1), 795774.7154594768)

