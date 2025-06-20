import unittest
from datasets.GPT_4.Zero_shot2.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_sort_1(self):
        self.assertEqual(sort_sublists([[3, 1], [2, 4]]), [[1, 3], [2, 4]])

    def test_sort_2(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_sort_3(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_4(self):
        self.assertEqual(sort_sublists([[], [2, 1]]), [[], [1, 2]])

    def test_sort_5(self):
        self.assertEqual(sort_sublists([[3], [1, 2, 0]]), [[3], [0, 1, 2]])

    def test_sort_6(self):
        self.assertEqual(sort_sublists([[2, 2], [1, 1]]), [[2, 2], [1, 1]])

    def test_sort_7(self):
        self.assertEqual(sort_sublists([[3, -1], [-2, 4]]), [[-1, 3], [-2, 4]])

