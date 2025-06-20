import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(zero_count([0, 1, 0, 2, 0, 3]), 1.5)

    def test_all_zeros(self):
        with self.assertRaises(ZeroDivisionError):
            zero_count([0, 0, 0])

    def test_no_zeros(self):
        self.assertEqual(zero_count([1, 2, 3, 4]), 0)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            zero_count([])

    def test_single_zero(self):
        with self.assertRaises(ZeroDivisionError):
            zero_count([0])

    def test_single_non_zero(self):
        self.assertEqual(zero_count([1]), 0)

    def test_large_list(self):
        large_list = [0] * 1000 + [1] * 1000
        self.assertEqual(zero_count(large_list), 1.0)

    def test_negative_numbers(self):
        self.assertEqual(zero_count([0, -1, 0, -2, 0, -3]), 1.5)

    def test_floating_point_numbers(self):
        with self.assertRaises(TypeError):
            zero_count([0, 1.5, 0, 2.5])

    def test_equal_zeros_non_zeros(self):
        self.assertEqual(zero_count([0, 1, 0, 2]), 1.0)

