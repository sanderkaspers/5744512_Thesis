import unittest
from datasets.o3.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_random_order(self):
        self.assertEqual(sort_matrix([[3,4],[1,2],[5]]), [[1,2],[3,4],[5]])

    def test_already_sorted(self):
        self.assertEqual(sort_matrix([[1],[2,1,0]]), [[1],[2,1,0]])

    def test_tie_sums_stable_order(self):
        self.assertEqual(sort_matrix([[1,1],[2]]), [[1,1],[2]])

    def test_negative_numbers(self):
        self.assertEqual(sort_matrix([[3,-3],[2,0],[1,1]]), [[3,-3],[1,1],[2,0]])

    def test_empty_matrix(self):
        self.assertEqual(sort_matrix([]), [])

    def test_single_row(self):
        self.assertEqual(sort_matrix([[9,1,0]]), [[9,1,0]])

