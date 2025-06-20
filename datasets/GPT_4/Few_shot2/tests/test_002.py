import unittest
from datasets.GPT_4.Few_shot2.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_sort_matrix_basic(self): self.assertEqual(sort_matrix([[3, 2, 1], [1, 2, 3], [4, 0, 0]]), [[4, 0, 0], [1, 2, 3], [3, 2, 1]])

    def test_sort_matrix_with_negative_numbers(self): self.assertEqual(sort_matrix([[1, -1], [-2, -2], [3, 0]]), [[-2, -2], [1, -1], [3, 0]])

    def test_sort_matrix_empty(self): self.assertEqual(sort_matrix([]), [])

    def test_sort_matrix_single_row(self): self.assertEqual(sort_matrix([[1, 2, 3]]), [[1, 2, 3]])

    def test_sort_matrix_all_rows_equal_sum(self): self.assertEqual(sort_matrix([[1, 2], [2, 1], [0, 3]]), [[1, 2], [2, 1], [0, 3]])

    def test_sort_matrix_all_zeros(self): self.assertEqual(sort_matrix([[0, 0], [0, 0]]), [[0, 0], [0, 0]])

    def test_sort_matrix_varied_lengths(self): self.assertEqual(sort_matrix([[1, 2, 3], [4], [1, 1]]), [[1, 1], [4], [1, 2, 3]])

    def test_sort_matrix_nested_empty(self): self.assertEqual(sort_matrix([[], [1], [0]]), [[], [0], [1]])

    def test_sort_matrix_large_numbers(self): self.assertEqual(sort_matrix([[100000, 200000], [300000], [50000, 25000]]), [[50000, 25000], [300000], [100000, 200000]])

    def test_sort_matrix_stability(self): self.assertEqual(sort_matrix([[1, 2], [2, 1], [3]]), [[1, 2], [2, 1], [3]])

