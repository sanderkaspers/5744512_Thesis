import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_triangle(self):
        expected = 3 * (2 ** 2) / (4 * tan(pi / 3))
        self.assertTrue(isclose(area_polygon(3, 2), expected, rel_tol=1e-9))

    def test_square(self):
        expected = 4 * (1 ** 2) / (4 * tan(pi / 4))
        self.assertTrue(isclose(area_polygon(4, 1), expected, rel_tol=1e-9))

    def test_hexagon(self):
        expected = 6 * (3 ** 2) / (4 * tan(pi / 6))
        self.assertTrue(isclose(area_polygon(6, 3), expected, rel_tol=1e-9))

    def test_large_sides(self):
        expected = 1000 * (1 ** 2) / (4 * tan(pi / 1000))
        self.assertTrue(isclose(area_polygon(1000, 1), expected, rel_tol=1e-9))

    def test_side_length_zero(self): self.assertEqual(area_polygon(6, 0), 0.0)

    def test_side_length_negative(self):
        result = area_polygon(6, -2)
        self.assertTrue(isinstance(result, float))

