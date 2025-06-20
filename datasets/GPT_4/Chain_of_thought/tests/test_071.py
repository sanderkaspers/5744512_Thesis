import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_typical_magic_square(self):
        matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        self.assertTrue(magic_square_test(matrix))

    def test_non_magic_square(self):
        matrix = [[8, 1, 6], [3, 5, 9], [4, 9, 2]]
        self.assertFalse(magic_square_test(matrix))

    def test_single_element_matrix(self):
        matrix = [[5]]
        self.assertTrue(magic_square_test(matrix))

    def test_matrix_with_zeroes(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertTrue(magic_square_test(matrix))

    def test_non_square_matrix(self):
        matrix = [[8, 1], [3, 5], [4, 9]]
        with self.assertRaises(IndexError):
            magic_square_test(matrix)

    def test_matrix_with_negative_numbers(self):
        matrix = [[-8, -1, -6], [-3, -5, -7], [-4, -9, -2]]
        self.assertTrue(magic_square_test(matrix))

    def test_large_magic_square(self):
        matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
        self.assertTrue(magic_square_test(matrix))

    def test_matrix_with_floats(self):
        matrix = [[8.0, 1.0, 6.0], [3.0, 5.0, 7.0], [4.0, 9.0, 2.0]]
        self.assertTrue(magic_square_test(matrix))

    def test_symmetric_but_non_magic(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertFalse(magic_square_test(matrix))

    def test_all_elements_same(self):
        matrix = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.assertFalse(magic_square_test(matrix))

