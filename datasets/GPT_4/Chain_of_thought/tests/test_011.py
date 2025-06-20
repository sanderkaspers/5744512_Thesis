import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_opposite_signs(self):
        self.assertTrue(opposite_Signs(10, -10))

    def test_both_positive(self):
        self.assertFalse(opposite_Signs(10, 20))

    def test_both_negative(self):
        self.assertFalse(opposite_Signs(-10, -20))

    def test_zero_and_positive(self):
        self.assertFalse(opposite_Signs(0, 10))

    def test_zero_and_negative(self):
        self.assertFalse(opposite_Signs(0, -10))

    def test_both_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

    def test_max_min_integers(self):
        self.assertTrue(opposite_Signs(2147483647, -2147483648))

    def test_large_values(self):
        self.assertTrue(opposite_Signs(123456789, -987654321))

    def test_small_values(self):
        self.assertTrue(opposite_Signs(1, -1))

    def test_large_positive_and_small_negative(self):
        self.assertTrue(opposite_Signs(1000000, -1))

    def test_equal_positive_negative(self):
        self.assertTrue(opposite_Signs(100, -100))

    def test_same_positive_twice(self):
        self.assertFalse(opposite_Signs(10, 10))

    def test_same_negative_twice(self):
        self.assertFalse(opposite_Signs(-10, -10))

    def test_floating_point_numbers(self):
        with self.assertRaises(TypeError):
            opposite_Signs(10.5, -10.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            opposite_Signs('10', '-10')

