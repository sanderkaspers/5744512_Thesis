import unittest
from datasets.GPT_4.Zero_shot2.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_sort_1(self):
        self.assertEqual(index_minimum([(1, 3), (2, 1), (3, 2)]), [(1, 3), (3, 2), (2, 1)])

    def test_sort_2(self):
        self.assertEqual(index_minimum([(1, 5), (2, 5), (3, 5)]), [(1, 5), (2, 5), (3, 5)])

    def test_sort_3(self):
        self.assertEqual(index_minimum([(1, 3), (2, 2), (3, 1)]), [(1, 3), (2, 2), (3, 1)])

    def test_sort_4(self):
        self.assertEqual(index_minimum([(3, 1), (2, 2), (1, 3)]), [(1, 3), (2, 2), (3, 1)])

    def test_sort_5(self):
        self.assertEqual(index_minimum([(1, -1), (2, -3), (3, -2)]), [(1, -1), (3, -2), (2, -3)])

    def test_sort_6(self):
        self.assertEqual(index_minimum([(1, -1), (2, 0), (3, 1)]), [(3, 1), (2, 0), (1, -1)])

    def test_sort_7(self):
        self.assertEqual(index_minimum([(1, 2.5), (2, 3.1), (3, 1.9)]), [(2, 3.1), (1, 2.5), (3, 1.9)])

    def test_sort_8(self):
        self.assertEqual(index_minimum([(1, 5)]), [(1, 5)])

    def test_sort_9(self):
        self.assertEqual(index_minimum([]), [])

    def test_sort_10(self):
        self.assertEqual(index_minimum([(1, 0), (2, -1), (3, 1)]), [(3, 1), (1, 0), (2, -1)])

    def test_sort_11(self):
        self.assertEqual(index_minimum([(1, "b"), (2, "a"), (3, "c")]), [(3, "c"), (1, "b"), (2, "a")])

    def test_sort_12(self):
        self.assertEqual(index_minimum([(1, 5, 7), (2, 3, 4)]), [(1, 5, 7), (2, 3, 4)])

    def test_sort_13(self):
        self.assertEqual(index_minimum([(1, 2), (2, 2), (3, 1)]), [(1, 2), (2, 2), (3, 1)])

    def test_sort_14(self):
        self.assertEqual(index_minimum([(2, 5), (1, 5)]), [(2, 5), (1, 5)])

    def test_sort_15(self):
        self.assertEqual(index_minimum([(1, 2), (2, 2.5), (3, 1)]), [(2, 2.5), (1, 2), (3, 1)])

