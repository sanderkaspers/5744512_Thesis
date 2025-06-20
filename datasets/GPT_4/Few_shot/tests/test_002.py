import unittest
from datasets.GPT_4.Few_shot.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sort_matrix([[3, 2, 1]]), [[3, 2, 1]])

    def test_case_2(self):
        self.assertEqual(sort_matrix([[3, 2, 1], [1, 2, 3], [2, 1, 3]]), [[1, 2, 3], [2, 1, 3], [3, 2, 1]])

    def test_case_3(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [1, 3, 2]]), [[1, 2, 3], [1, 3, 2]])

    def test_case_4(self):
        self.assertEqual(sort_matrix([]), [])

    def test_case_5(self):
        self.assertEqual(sort_matrix([[5, 4], [2, 3], [9]]), [[2, 3], [5, 4], [9]])

    def test_case_6(self):
        self.assertEqual(sort_matrix([[3], [1], [2]]), [[1], [2], [3]])

    def test_case_7(self):
        self.assertEqual(sort_matrix([[2, 2], [2, 1], [2, 3]]), [[2, 2], [2, 1], [2, 3]])

