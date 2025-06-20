import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Volume(3, 4, 5), 30)

    def test_zero_length(self):
        self.assertEqual(find_Volume(0, 4, 5), 0)

    def test_zero_base(self):
        self.assertEqual(find_Volume(3, 0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(find_Volume(3, 4, 0), 0)

    def test_negative_length(self):
        self.assertEqual(find_Volume(-3, 4, 5), -30)

    def test_negative_base(self):
        self.assertEqual(find_Volume(3, -4, 5), -30)

    def test_negative_height(self):
        self.assertEqual(find_Volume(3, 4, -5), -30)

    def test_all_negative(self):
        self.assertEqual(find_Volume(-3, -4, -5), -30)

    def test_floating_point_values(self):
        self.assertAlmostEqual(find_Volume(3.5, 4.1, 5.2), 37.31, places=2)

    def test_large_numbers(self):
        self.assertEqual(find_Volume(1e6, 1e6, 1e6), 5e17)

    def test_small_numbers(self):
        self.assertAlmostEqual(find_Volume(1e-6, 1e-6, 1e-6), 5e-19, places=25)

    def test_boundary_values(self):
        self.assertAlmostEqual(find_Volume(1e-6, 4, 5), 1e-6 * 4 * 5 / 2, places=10)

    def test_one_dimension(self):
        self.assertEqual(find_Volume(1, 4, 5), 10)

    def test_all_dimensions_one(self):
        self.assertEqual(find_Volume(1, 1, 1), 0.5)

    def test_equal_dimensions(self):
        self.assertEqual(find_Volume(5, 5, 5), 62.5)

    def test_high_precision_floats(self):
        self.assertAlmostEqual(find_Volume(1.123456789, 2.987654321, 4.567890123), 7.680831123, places=9)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            find_Volume('3', 4, 5)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            find_Volume(None, 4, 5)

    def test_empty_string_input(self):
        with self.assertRaises(TypeError):
            find_Volume('', 4, 5)

