import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_typical_positive_integer(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_zero_value(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_value(self):
        self.assertEqual(square_perimeter(-5), -20)

    def test_floating_point_value(self):
        self.assertEqual(square_perimeter(2.5), 10.0)

    def test_large_value(self):
        self.assertEqual(square_perimeter(1e6), 4e6)

    def test_small_value(self):
        self.assertEqual(square_perimeter(1e-6), 4e-6)

    def test_boundary_value(self):
        self.assertEqual(square_perimeter(1), 4)

    def test_high_precision_float(self):
        self.assertEqual(square_perimeter(1.123456789), 4.493827156)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            square_perimeter('5')

    def test_list_input(self):
        with self.assertRaises(TypeError):
            square_perimeter([5])

    def test_infinity(self):
        self.assertEqual(square_perimeter(float('inf')), float('inf'))

    def test_nan(self):
        self.assertTrue(isnan(square_perimeter(float('nan'))))

    def test_none_input(self):
        with self.assertRaises(TypeError):
            square_perimeter(None)

    def test_complex_number(self):
        self.assertEqual(square_perimeter(1 + 2j), 4 + 8j)

