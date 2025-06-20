import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_num([1, 2, 3, 4]), 6.0)

    def test_single_element(self):
        self.assertEqual(multiply_num([5]), 5.0)

    def test_list_with_zero(self):
        self.assertEqual(multiply_num([1, 2, 0, 4]), 0.0)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

    def test_list_with_negative_numbers(self):
        self.assertEqual(multiply_num([-1, 2, -3, 4]), 1.5)

    def test_mixed_numbers(self):
        self.assertEqual(multiply_num([-1, 2, 3, -4]), 1.5)

    def test_floating_point_numbers(self):
        self.assertEqual(multiply_num([1.5, 2.5, 3.5]), 3.75)

    def test_large_numbers(self):
        self.assertEqual(multiply_num([100000, 100000]), 10000000000.0)

    def test_list_with_one(self):
        self.assertEqual(multiply_num([1, 1, 1, 1]), 1.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            multiply_num(['1', 2, 3, 4])

