import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_triangle(self): self.assertTrue(isclose(area_polygon(3, 1), 0.4330127, rel_tol=1e-5))

    def test_square(self): self.assertEqual(area_polygon(4, 2), 4.0)

    def test_pentagon(self): self.assertTrue(isclose(area_polygon(5, 1), 1.72048, rel_tol=1e-4))

    def test_hexagon(self): self.assertTrue(isclose(area_polygon(6, 1), 2.5980762, rel_tol=1e-5))

    def test_circle_approximation(self): self.assertTrue(isclose(area_polygon(1000, 1), 796.178, rel_tol=1e-3))

    def test_large_side_length(self): self.assertEqual(area_polygon(4, 100), 2500.0)

    def test_zero_length(self): self.assertEqual(area_polygon(4, 0), 0.0)

    def test_negative_length(self): self.assertEqual(area_polygon(4, -2), 4.0)

    def test_float_inputs(self): self.assertTrue(isclose(area_polygon(6.0, 2.5), 16.237, rel_tol=1e-3))

