import unittest
from datasets.GPT_4.Zero_shot2.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_sort_matrix_1(self):
        self.assertEqual(sort_matrix([[3, 4], [1, 2], [6]]), [[1, 2], [3, 4], [6]])

    def test_sort_matrix_2(self):
        self.assertEqual(sort_matrix([[1, 1], [2], [0, 2]]), [[1, 1], [2], [0, 2]])

    def test_sort_matrix_3(self):
        self.assertEqual(sort_matrix([[1, -2], [-1, -1], [0, 0]]), [[-1, -1], [0, 0], [1, -2]])

    def test_sort_matrix_4(self):
        self.assertEqual(sort_matrix([[], [1], [1, 2]]), [[], [1], [1, 2]])

    def test_sort_matrix_5(self):
        self.assertEqual(sort_matrix([[1, 2, 3]]), [[1, 2, 3]])

    def test_sort_matrix_6(self):
        self.assertEqual(sort_matrix([[1, 1], [1, 1], [1, 1]]), [[1, 1], [1, 1], [1, 1]])

