import unittest
from datasets.GPT_4.Zero_shot1.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sort_matrix([[10], [2, 3], [1, 1, 1]]), [[1, 1, 1], [2, 3], [10]])

    def test_2(self):
        self.assertEqual(sort_matrix([[5, 5], [3, 7], [0, 10]]), [[5, 5], [3, 7], [0, 10]])

    def test_3(self):
        self.assertEqual(sort_matrix([[3, 3], [2, 2], [1, 1]]), [[1, 1], [2, 2], [3, 3]])

    def test_4(self):
        self.assertEqual(sort_matrix([[], [1], [1, 2, 3]]), [[], [1], [1, 2, 3]])

    def test_5(self):
        self.assertEqual(sort_matrix([[1, -1], [-2, 2], [0, 0]]), [[1, -1], [-2, 2], [0, 0]])

    def test_6(self):
        self.assertEqual(sort_matrix([[0], [0, 0], [0, 0, 0]]), [[0], [0, 0], [0, 0, 0]])

    def test_7(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [4, -1, 0], [2, 2]]), [[2, 2], [4, -1, 0], [1, 2, 3]])

    def test_8(self):
        self.assertEqual(sort_matrix([[100], [50, 50], [25, 25, 50]]), [[25, 25, 50], [50, 50], [100]])

    def test_9(self):
        self.assertEqual(sort_matrix([]), [])

