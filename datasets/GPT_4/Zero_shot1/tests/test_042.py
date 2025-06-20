import unittest
from datasets.GPT_4.Zero_shot1.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(index_max_tuple([(1, 2), (3, 4), (5, 0)], 0), (5, 0))

    def test_2(self):
        self.assertEqual(index_max_tuple([(1, 2), (3, 4), (5, 4)], 1), (3, 4))

    def test_3(self):
        self.assertEqual(index_max_tuple([(9, 2), (5, 4)], 0), (9, 2))

    def test_4(self):
        self.assertEqual(index_max_tuple([(1, 20), (3, 40)], 1), (3, 40))

    def test_5(self):
        self.assertEqual(index_max_tuple([(99, 1), (1, 2)], 0), (99, 1))

    def test_6(self):
        self.assertEqual(index_max_tuple([(1, 2, 3), (3, 4, 9)], 2), (3, 4, 9))

    def test_7(self):
        self.assertEqual(index_max_tuple([(-1, -2), (-3, -1)], 1), (-3, -1))

    def test_8(self):
        self.assertEqual(index_max_tuple([(1.5, 2), (1.1, 3.3)], 1), (1.1, 3.3))

    def test_9(self):
        self.assertEqual(index_max_tuple([("a", 2), ("z", 1)], 0), ("z", 1))

    def test_10(self):
        self.assertEqual(index_max_tuple([(1, 1), (2, 1), (3, 1)], 1), (1, 1))

    def test_11(self):
        self.assertEqual(index_max_tuple([(42, 99)], 1), (42, 99))

    def test_12(self):
        big_list = [(i, i**2) for i in range(1000)]
        self.assertEqual(index_max_tuple(big_list, 1), (999, 998001))

    def test_13(self):
        self.assertEqual(index_max_tuple([((1,), 2), ((2,), 3)], 1), ((2,), 3))

    def test_14(self):
        self.assertEqual(index_max_tuple([(True,), (False,)], 0), (True,))

