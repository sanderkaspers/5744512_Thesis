import unittest
from datasets.GPT_4.Few_shot1.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_max_product_tuple_basic(self): self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), 12)

    def test_max_product_tuple_negative_values(self): self.assertEqual(max_product_tuple([(-1, 5), (3, -2)]), 5)

    def test_max_product_tuple_all_negatives(self): self.assertEqual(max_product_tuple([(-1, -1), (-2, -3)]), 6)

    def test_max_product_tuple_zero_in_tuple(self): self.assertEqual(max_product_tuple([(0, 5), (3, 0)]), 0)

    def test_max_product_tuple_mixed_signs(self): self.assertEqual(max_product_tuple([(1, -10), (2, 3)]), 10)

    def test_max_product_tuple_single_pair(self): self.assertEqual(max_product_tuple([(7, 2)]), 14)

    def test_max_product_tuple_large_numbers(self): self.assertEqual(max_product_tuple([(1000, 2000), (-3000, -4000)]), 12000000)

