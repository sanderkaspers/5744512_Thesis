import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(6, 10), 259.8076, places=4)

    def test_minimum_sides(self):
        self.assertAlmostEqual(area_polygon(3, 10), 43.3013, places=4)

    def test_large_number_of_sides(self):
        self.assertAlmostEqual(area_polygon(1000, 10), 79577.2087, places=4)

    def test_zero_side_length(self):
        self.assertEqual(area_polygon(6, 0), 0)

    def test_negative_side_length(self):
        with self.assertRaises(ValueError):
            area_polygon(6, -10)

    def test_negative_number_of_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-6, 10)

    def test_floating_point_inputs(self):
        self.assertAlmostEqual(area_polygon(6.5, 10.5), 284.3015, places=4)

    def test_very_small_side_length(self):
        self.assertAlmostEqual(area_polygon(6, 0.001), 0.0000002598, places=10)

    def test_string_input_for_sides(self):
        with self.assertRaises(TypeError):
            area_polygon('6', 10)

    def test_non_integer_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(3.5, 10)

