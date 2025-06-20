import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_all_positive(self): self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), 30)

    def test_with_negatives(self): self.assertEqual(max_product_tuple([(-1, 10), (-2, -3), (4, -5)]), 20)

    def test_with_zeros(self): self.assertEqual(max_product_tuple([(0, 99), (5, 0), (0, 0)]), 0)

    def test_with_mix(self): self.assertEqual(max_product_tuple([(1, -100), (2, 50), (-5, -5)]), 100)

    def test_equal_products(self): self.assertEqual(max_product_tuple([(2, 3), (-3, -2), (1, -6)]), 6)

    def test_single_tuple(self): self.assertEqual(max_product_tuple([(7, -8)]), 56)

    def test_float_inputs(self): self.assertEqual(max_product_tuple([(1.5, -2.0), (3.0, 1.1)]), 3.3)

    def test_large_numbers(self): self.assertEqual(max_product_tuple([(100000, 3000), (50000, 8000)]), 400000000)

