import unittest
from datasets.GPT_4.Few_shot.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), (5, 6))   # Maximum product is 30)

    def test_case_2(self):
        self.assertEqual(max_product_tuple([(-1, -2), (3, 4), (5, -6)]), (3, 4) )  # Mixed positive and negative)

    def test_case_3(self):
        self.assertEqual(max_product_tuple([(1, 0), (3, 4), (5, 6)]), (5, 6) )  # Zero in tuple)

    def test_case_4(self):
        self.assertEqual(max_product_tuple([(0, 0), (0, 0), (0, 0)]), (0, 0))   # All zeros)

    def test_case_5(self):
        self.assertEqual(max_product_tuple([(10, 10), (1, 100), (100, 1)]), (10, 10))   # Equal products)

    def test_case_6(self):
        self.assertEqual(max_product_tuple([(1, 2)]), (1, 2))   # Single tuple)

    def test_case_7(self):
        self.assertEqual(max_product_tuple([(-5, 6), (-7, 8), (-9, 10)]), (-9, 10))   # Negative and positive mixed)

    def test_case_8(self):
        self.assertEqual(max_product_tuple([(100, 0), (1, 2), (0, 100)]), (1, 2))   # Products are equal but not maximum)

