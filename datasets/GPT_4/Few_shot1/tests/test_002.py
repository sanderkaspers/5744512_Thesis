import unittest
from datasets.GPT_4.Few_shot1.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_sort_matrix_empty(self): self.assertEqual(sort_matrix([]), [])

    def test_sort_matrix_single_row(self): self.assertEqual(sort_matrix([[3, 2, 1]]), [[3, 2, 1]])

    def test_sort_matrix_same_sum_rows(self): self.assertEqual(sort_matrix([[1, 2], [2, 1]]), [[1, 2], [2, 1]])

    def test_sort_matrix_distinct_sums(self): self.assertEqual(sort_matrix([[3, 4], [1, 2], [5, 0]]), [[1, 2], [5, 0], [3, 4]])

    def test_sort_matrix_negative_values(self): self.assertEqual(sort_matrix([[3, -1], [2, -3], [-2, -2]]), [[2, -3], [-2, -2], [3, -1]])

    def test_sort_matrix_with_zero_rows(self): self.assertEqual(sort_matrix([[0, 0], [1, -1], [2, 2]]), [[0, 0], [1, -1], [2, 2]])

    def test_sort_matrix_mixed_row_lengths(self): self.assertEqual(sort_matrix([[1, 2], [1], [2, 2]]), [[1], [1, 2], [2, 2]])

    def test_sort_matrix_all_zero_rows(self): self.assertEqual(sort_matrix([[0, 0], [0, 0], [0, 0]]), [[0, 0], [0, 0], [0, 0]])

    def test_sort_matrix_large_numbers(self): self.assertEqual(sort_matrix([[1000000, 2], [999999, 3], [1, 1000001]]), [[999999, 3], [1000000, 2], [1, 1000001]])

    def test_sort_matrix_single_column_rows(self): self.assertEqual(sort_matrix([[3], [1], [2]]), [[1], [2], [3]])

