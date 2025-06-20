import unittest
from datasets.GPT_4.Few_shot2.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_max_product_tuple_basic(self): self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), (3, 4))

    def test_max_product_tuple_negative_values(self): self.assertEqual(max_product_tuple([(-1, -2), (-3, -1)]), (-3, -1))

    def test_max_product_tuple_with_zero(self): self.assertEqual(max_product_tuple([(0, 1), (2, 0)]), (0, 1))

    def test_max_product_tuple_single_tuple(self): self.assertEqual(max_product_tuple([(7, 8)]), (7, 8))

    def test_max_product_tuple_multiple_max(self): self.assertEqual(max_product_tuple([(2, 3), (3, 2)]), (2, 3))

    def test_max_product_tuple_all_zeros(self): self.assertEqual(max_product_tuple([(0, 0), (0, 0)]), (0, 0))

    def test_max_product_tuple_empty_list(self): self.assertEqual(max_product_tuple([]), ())

    def test_max_product_tuple_with_one_empty_tuple(self): self.assertEqual(max_product_tuple([(1, 2), ()]), (1, 2))

    def test_max_product_tuple_all_empty(self): self.assertEqual(max_product_tuple([(), ()]), ())

