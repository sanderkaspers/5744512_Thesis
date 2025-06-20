import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(pos_count([1, -2, 3, 0, -5, 7]), 4)

    def test_all_positive_numbers(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)

    def test_all_negative_numbers(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_list_with_zero(self):
        self.assertEqual(pos_count([0]), 1)

    def test_all_zeros(self):
        self.assertEqual(pos_count([0, 0, 0]), 3)

    def test_single_positive_number(self):
        self.assertEqual(pos_count([7]), 1)

    def test_single_negative_number(self):
        self.assertEqual(pos_count([-3]), 0)

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_large_positive_numbers(self):
        self.assertEqual(pos_count([1000000, 2000000, 3000000]), 3)

    def test_large_negative_numbers(self):
        self.assertEqual(pos_count([-1000000, -2000000, -3000000]), 0)

    def test_mixed_positive_negative(self):
        self.assertEqual(pos_count([-1, 0, 1]), 2)

    def test_floating_point_numbers(self):
        self.assertEqual(pos_count([1.5, -2.5, 0.0, 3.7]), 3)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            pos_count([1, 'two', 3.0])

    def test_max_min_integers(self):
        self.assertEqual(pos_count([2147483647, -2147483648]), 1)

