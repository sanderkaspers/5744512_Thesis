import unittest
from datasets.o3.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer_side(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_float_side(self):
        self.assertEqual(square_perimeter(2.5), 10.0)

    def test_zero_side(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_side(self):
        self.assertEqual(square_perimeter(-4), -16)

    def test_large_edge(self):
        self.assertEqual(square_perimeter(1000000), 4000000)

    def test_non_numeric_type_error(self):
        with self.assertRaises(TypeError):
            square_perimeter("a")

