import unittest
from datasets.GPT_4.Zero_shot1.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (2, 5)]), (3, 4))

    def test_2(self):
        self.assertEqual(max_product_tuple([(2, 2), (1, 4)]), (2, 2))

    def test_3(self):
        self.assertEqual(max_product_tuple([(0, 10), (5, 5)]), (5, 5))

    def test_4(self):
        self.assertEqual(max_product_tuple([(-2, 3), (4, -1)]), (-2, 3))

    def test_5(self):
        self.assertEqual(max_product_tuple([(-5, -5), (2, 2)]), (-5, -5))

    def test_6(self):
        self.assertEqual(max_product_tuple([(9, 9)]), (9, 9))

    def test_7(self):
        self.assertEqual(max_product_tuple([(0, 0), (0, 1)]), (0, 1))

    def test_8(self):
        self.assertEqual(max_product_tuple([(10000, 1), (10, 2000)]), (10, 2000))

    def test_9(self):
        result = max_product_tuple([(3, 3), (1, 9)])
        self.assertIsInstance(result, tuple)

