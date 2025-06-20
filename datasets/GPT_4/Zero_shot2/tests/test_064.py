import unittest
from datasets.GPT_4.Zero_shot2.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_max_1(self):
        self.assertEqual(max_product_tuple([(1,2), (3,4)]), (3,4))

    def test_max_2(self):
        self.assertEqual(max_product_tuple([(-1,-2), (3,1)]), (-1,-2))

    def test_max_3(self):
        self.assertEqual(max_product_tuple([(0,5), (1,1)]), (1,1))

    def test_max_4(self):
        self.assertEqual(max_product_tuple([(2,3), (3,2)]), (3,2))

    def test_max_5(self):
        self.assertEqual(max_product_tuple([(7,1)]), (7,1))

    def test_max_6(self):
        self.assertEqual(max_product_tuple([(), (1,2)]), (1,2))

    def test_max_7(self):
        self.assertEqual(max_product_tuple([]), ())

