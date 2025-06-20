import unittest
from datasets.GPT_4.Zero_shot1.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [5, 4]]), [[1, 2, 3], [4, 5]])

    def test_2(self):
        self.assertEqual(sort_sublists([[1], [3, 2], [5, 0, 9]]), [[1], [2, 3], [0, 5, 9]])

    def test_3(self):
        self.assertEqual(sort_sublists([[], [3], []]), [[], [3], []])

    def test_4(self):
        self.assertEqual(sort_sublists([]), [])

    def test_5(self):
        self.assertEqual(sort_sublists([[2, 2, 1], [4, 4, 4]]), [[1, 2, 2], [4, 4, 4]])

    def test_6(self):
        self.assertEqual(sort_sublists([[-3, -1, -2]]), [[-3, -2, -1]])

    def test_7(self):
        result = sort_sublists([[3, 1]])
        self.assertIsInstance(result, list)

