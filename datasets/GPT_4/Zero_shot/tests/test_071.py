import unittest
from datasets.GPT_4.Zero_shot.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        my_matrix = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
        ]
        expected_output = True  # This is a valid magic square
        assert magic_square_test(my_matrix) == expected_output

    def test_multiple_spaces_2(self):
        my_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
        expected_output = False  # This is not a magic square
        assert magic_square_test(my_matrix) == expected_output

    def test_multiple_spaces_3(self):
        my_matrix = [[5]]
        expected_output = True  # A 1x1 matrix is trivially a magic square
        assert magic_square_test(my_matrix) == expected_output

    def test_multiple_spaces_4(self):
        my_matrix = []
        expected_output = False  # An empty matrix should not be considered a magic square
        assert magic_square_test(my_matrix) == expected_output

    def test_multiple_spaces_5(self):
        my_matrix = [
        [1, 2, 3],
        [4, 5, 6]
        ]
        expected_output = False  # This is not a square matrix
        assert magic_square_test(my_matrix) == expected_output

    def test_multiple_spaces_6(self):
        my_matrix = [
        [-2, -7, -6],
        [-9, -5, -1],
        [-4, -3, -8]
        ]
        expected_output = True  # This is a valid magic square with negative numbers
        assert magic_square_test(my_matrix) == expected_output

    def test_multiple_spaces_7(self):
        my_matrix = [
        [17, 24, 1, 8, 15],
        [23, 5, 7, 14, 16],
        [4, 6, 13, 20, 22],
        [10, 12, 19, 21, 3],
        [11, 18, 25, 2, 9]
        ]
        expected_output = True  # A larger valid magic square (5x5)
        assert magic_square_test(my_matrix) == expected_output

