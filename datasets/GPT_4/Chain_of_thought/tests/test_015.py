import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_difference([(1, 5), (2, 8), (3, 4)]), 6)

    def test_single_pair(self):
        self.assertEqual(max_difference([(1, 5)]), 4)

    def test_all_identical_pairs(self):
        self.assertEqual(max_difference([(3, 3), (3, 3), (3, 3)]), 0)

    def test_negative_values(self):
        self.assertEqual(max_difference([(-5, -1), (-8, -2), (-4, -3)]), 7)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_difference([(-2, 5), (4, -4), (1, -1)]), 9)

    def test_zero_difference(self):
        self.assertEqual(max_difference([(7, 7), (0, 0), (-5, -5)]), 0)

    def test_large_numbers(self):
        self.assertEqual(max_difference([(1000000, 5000000), (100000, 500000)]), 4000000)

    def test_small_numbers(self):
        self.assertEqual(max_difference([(0.0001, 0.0005), (0.0002, 0.0008)]), 0.0006)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_difference([])

    def test_floating_point_numbers(self):
        self.assertEqual(max_difference([(2.5, 3.5), (3.1, 1.1)]), 1.0)

    def test_single_element_tuples(self):
        with self.assertRaises(ValueError):
            max_difference([(1,)])

    def test_max_min_integers(self):
        self.assertEqual(max_difference([(2147483647, -2147483648), (-2147483648, 2147483647)]), 4294967295)

