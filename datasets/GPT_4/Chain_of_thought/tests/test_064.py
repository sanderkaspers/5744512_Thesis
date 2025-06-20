import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), 30)

    def test_negative_numbers(self):
        self.assertEqual(max_product_tuple([(-1, -2), (-3, -4), (-5, -6)]), 30)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_product_tuple([(1, -2), (-3, 4), (5, -6)]), 30)

    def test_zero_in_tuples(self):
        self.assertEqual(max_product_tuple([(0, 2), (3, 0), (0, 0)]), 0)

    def test_single_tuple(self):
        self.assertEqual(max_product_tuple([(3, 4)]), 12)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_product_tuple([])

    def test_large_numbers(self):
        self.assertEqual(max_product_tuple([(10**10, 10**10), (10**9, 10**9)]), 10**20)

    def test_identical_elements(self):
        self.assertEqual(max_product_tuple([(2, 2), (3, 3), (4, 4)]), 16)

    def test_floating_point_numbers(self):
        self.assertEqual(max_product_tuple([(1.5, 2.5), (3.5, 4.5), (5.5, 6.5)]), 35.75)

    def test_one_as_element(self):
        self.assertEqual(max_product_tuple([(1, 100), (1, 200), (1, 300)]), 300)

