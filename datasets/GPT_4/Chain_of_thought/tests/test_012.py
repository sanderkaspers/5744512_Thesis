import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(is_octagonal(5), 65)

    def test_zero_input(self):
        self.assertEqual(is_octagonal(0), 0)

    def test_negative_input(self):
        self.assertEqual(is_octagonal(-3), -39)

    def test_large_positive_number(self):
        self.assertEqual(is_octagonal(1000), 2998000)

    def test_small_positive_number(self):
        self.assertEqual(is_octagonal(1), 1)

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            is_octagonal(2.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            is_octagonal('10')

    def test_boundary_n_2(self):
        self.assertEqual(is_octagonal(2), 10)

    def test_fractional_input(self):
        with self.assertRaises(TypeError):
            is_octagonal(3.7)

    def test_first_few_octagonal_numbers(self):
        self.assertEqual(is_octagonal(1), 1)
        self.assertEqual(is_octagonal(2), 10)
        self.assertEqual(is_octagonal(3), 27)
        self.assertEqual(is_octagonal(4), 52)
        self.assertEqual(is_octagonal(5), 85)

