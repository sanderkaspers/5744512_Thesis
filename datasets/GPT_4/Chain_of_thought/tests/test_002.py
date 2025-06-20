import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_varying_row_sums(self):
        matrix = [[3, 1, 2], [1, 2, 3], [4, 4, 4]]
        expected = [[1, 2, 3], [3, 1, 2], [4, 4, 4]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_single_row(self):
        matrix = [[3, 1, 2]]
        expected = [[3, 1, 2]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_single_column(self):
        matrix = [[3], [1], [2]]
        expected = [[1], [2], [3]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_all_zero_rows(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_identical_rows(self):
        matrix = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        expected = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(sort_matrix(matrix), expected)

    def test_negative_numbers(self):
        matrix = [[-1, -2, -3], [1, 2, 3], [0, 0, 0]]
        expected = [[-1, -2, -3], [0, 0, 0], [1, 2, 3]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_mixed_numbers(self):
        matrix = [[1, -2, 3], [-1, 2, -3], [0, 0, 0]]
        expected = [[-1, 2, -3], [0, 0, 0], [1, -2, 3]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_floating_point_numbers(self):
        matrix = [[1.5, 2.5, 3.5], [1.2, 2.2, 3.2], [1.1, 2.1, 3.1]]
        expected = [[1.1, 2.1, 3.1], [1.2, 2.2, 3.2], [1.5, 2.5, 3.5]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_large_matrix(self):
        matrix = [[i for i in range(1000)], [i for i in range(1000, 2000)]]
        expected = [[i for i in range(1000)], [i for i in range(1000, 2000)]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_rows_with_same_sum(self):
        matrix = [[2, 3], [1, 4]]
        expected = [[2, 3], [1, 4]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_single_element_matrix(self):
        matrix = [[42]]
        expected = [[42]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_uneven_rows(self):
        matrix = [[1, 2, 3], [4, 5], [6]]
        expected = [[6], [4, 5], [1, 2, 3]]
        self.assertEqual(sort_matrix(matrix), expected)

    def test_already_sorted_matrix(self):
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(sort_matrix(matrix), expected)

