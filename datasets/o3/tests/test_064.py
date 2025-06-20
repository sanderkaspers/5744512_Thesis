import unittest
from datasets.o3.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_positive_pairs(self):
        self.assertEqual(max_product_tuple([(1,2),(3,4)]), 12)

    def test_negative_and_positive(self):
        self.assertEqual(max_product_tuple([(-10,3),(2,5)]), 30)

    def test_zero_in_pairs(self):
        self.assertEqual(max_product_tuple([(0,99),(1,1)]), 1)

    def test_duplicate_max_product(self):
        self.assertEqual(max_product_tuple([(-3,-5),(3,5)]), 15)

    def test_single_pair(self):
        self.assertEqual(max_product_tuple([(7,8)]), 56)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            max_product_tuple([])

