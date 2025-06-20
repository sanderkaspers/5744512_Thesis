import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_typical(self): self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 1)]), (3, 4))

    def test_max_at_start(self): self.assertEqual(max_product_tuple([(10, 10), (2, 3), (4, 4)]), (10, 10))

    def test_max_at_end(self): self.assertEqual(max_product_tuple([(1, 2), (2, 3), (10, 5)]), (10, 5))

    def test_zero_product(self): self.assertEqual(max_product_tuple([(0, 1), (2, 0), (3, 4)]), (3, 4))

    def test_negative_numbers(self): self.assertEqual(max_product_tuple([(-1, -2), (-3, 1), (-2, 2)]), (-1, -2))

    def test_equal_products(self): self.assertEqual(max_product_tuple([(2, 3), (3, 2), (1, 6)]), (2, 3))

    def test_single_tuple(self): self.assertEqual(max_product_tuple([(9, 9)]), (9, 9))

    def test_large_numbers(self): self.assertEqual(max_product_tuple([(100000, 300000), (1, 2)]), (100000, 300000))

    def test_tie_max(self): self.assertEqual(max_product_tuple([(4, 5), (5, 4)]), (4, 5))

    def test_float_and_int(self): self.assertEqual(max_product_tuple([(1.5, 2), (2, 1)]), (1.5, 2))

    def test_zero_negative(self): self.assertEqual(max_product_tuple([(-3, 0), (-2, 2)]), (-2, 2))

