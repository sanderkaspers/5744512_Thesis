import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(centered_hexagonal_number(5), 61)

    def test_zero_input(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            centered_hexagonal_number(-3)

    def test_large_number(self):
        self.assertEqual(centered_hexagonal_number(1000), 2997001)

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(5.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number('10')

    def test_max_integer(self):
        self.assertTrue(centered_hexagonal_number(2147483647) > 0)

