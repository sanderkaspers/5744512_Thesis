import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(hexagonal_num(5), 45)

    def test_n_equals_1(self):
        self.assertEqual(hexagonal_num(1), 1)

    def test_n_equals_0(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            hexagonal_num(-3)

    def test_large_n(self):
        self.assertEqual(hexagonal_num(100000), 19999900000)

    def test_floating_point_n(self):
        with self.assertRaises(TypeError):
            hexagonal_num(2.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            hexagonal_num('5')

    def test_n_equals_2(self):
        self.assertEqual(hexagonal_num(2), 6)

    def test_maximum_n(self):
        self.assertEqual(hexagonal_num(1000000), 1999999000000)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            hexagonal_num(4.0)

