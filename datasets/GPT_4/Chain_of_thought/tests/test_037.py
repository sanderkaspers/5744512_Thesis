import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(closest_num(10), 9)

    def test_zero_input(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative_number(self):
        self.assertEqual(closest_num(-3), -4)

    def test_large_number(self):
        self.assertEqual(closest_num(1000000), 999999)

    def test_small_number(self):
        self.assertEqual(closest_num(1), 0)

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            closest_num(5.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            closest_num('10')

    def test_max_integer(self):
        self.assertEqual(closest_num(2147483647), 2147483646)

    def test_min_integer(self):
        self.assertEqual(closest_num(-2147483648), -2147483649)

