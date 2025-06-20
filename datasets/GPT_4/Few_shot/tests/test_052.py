import unittest
from datasets.GPT_4.Few_shot.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sort_sublists([[3, 1, 2], [9, 7, 8]]), [[1, 2, 3], [7, 8, 9]]) # Standard case)

    def test_case_2(self):
        self.assertEqual(sort_sublists([[1], [3], [2]]), [[1], [3], [2]]) # Single-element sublists)

    def test_case_3(self):
        self.assertEqual(sort_sublists([[1.5, 2.5, 0.5], [-1, 0, 1]]), [[0.5, 1.5, 2.5], [-1, 0, 1]]) # Floats and negatives)

    def test_case_4(self):
        self.assertEqual(sort_sublists([[], [1, 3, 2], [5, 4]]), [[], [1, 2, 3], [4, 5]]) # Empty sublist)

    def test_case_5(self):
        self.assertEqual(sort_sublists([[10, -10, 5, 0]]), [[-10, 0, 5, 10]]) # Mixed integers)

    def test_case_6(self):
        self.assertEqual(sort_sublists([[3, 3, 3], [2, 2, 2]]), [[3, 3, 3], [2, 2, 2]]) # Identical elements)

    def test_case_7(self):
        self.assertEqual(sort_sublists([[2], [], [1]]), [[2], [], [1]]) # Mixed empty and single-element lists)

    def test_case_8(self):
        self.assertEqual(sort_sublists([[7, 5, 2, 4, 1], [9, 8, 0]]), [[1, 2, 4, 5, 7], [0, 8, 9]]) # Mixed sizes)

