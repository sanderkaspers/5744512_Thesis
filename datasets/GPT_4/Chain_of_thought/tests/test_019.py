import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(bell_number(5), 52)

    def test_zero_input(self):
        self.assertEqual(bell_number(0), 1)

    def test_large_number(self):
        self.assertEqual(bell_number(10), 115975)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            bell_number(-1)

    def test_boundary_n_1(self):
        self.assertEqual(bell_number(1), 1)

    def test_boundary_n_2(self):
        self.assertEqual(bell_number(2), 2)

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            bell_number(2.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            bell_number('10')

    def test_large_number_performance(self):
        self.assertTrue(bell_number(20) > 0)

