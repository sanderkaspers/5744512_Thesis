import unittest
from datasets.GPT_4.Zero_shot.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this__to_sort(self):
        M = [[3, 2, 1], [1, 2, 3], [4, 5, 6]]
        expected_output = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
        assert sort_matrix(M) == expected_output

    def test_write_all_the__cases_for_this__to_sort_1(self):
        M = [[1, 1, 1], [2, 2], [3, 0, 0]]
        expected_output = [[1, 1, 1], [3, 0, 0], [2, 2]]
        assert sort_matrix(M) == expected_output

    def test_write_all_the__cases_for_this__to_sort_2(self):
        M = [[1, 2, 3]]
        expected_output = [[1, 2, 3]]
        assert sort_matrix(M) == expected_output

    def test_multiple_spaces_4(self):
        M = []
        expected_output = []
        assert sort_matrix(M) == expected_output

    def test_multiple_spaces_5(self):
        M = [[3, 3], [], [1, 1, 1]]
        expected_output = [[], [1, 1, 1], [3, 3]]
        assert sort_matrix(M) == expected_output

    def test_write_all_the__cases_for_this__to_sort_3(self):
        M = [[0, 0, 0], [0, 0], [0]]
        expected_output = [[0], [0, 0], [0, 0, 0]]
        assert sort_matrix(M) == expected_output

    def test_write_all_the__cases_for_this__to_sort_4(self):
        M = [[1, 2], [1, 2, 3], [1]]
        expected_output = [[1], [1, 2], [1, 2, 3]]
        assert sort_matrix(M) == expected_output

