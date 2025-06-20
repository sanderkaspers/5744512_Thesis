import unittest
from datasets.GPT_4.Zero_shot.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        arr = [1, -2, 3, 4]
        expected_output = 6  # Max absolute difference is between -2 and 4
        assert max_Abs_Diff(arr) == expected_output

    def test_multiple_spaces_2(self):
        arr = [2, 3, 10, 6]
        expected_output = 8  # Max absolute difference is between 2 and 10
        assert max_Abs_Diff(arr) == expected_output

    def test_multiple_spaces_3(self):
        arr = [-1, -4, -7]
        expected_output = 6  # Max absolute difference is between -1 and -7
        assert max_Abs_Diff(arr) == expected_output

    def test_multiple_spaces_4(self):
        arr = [7]
        expected_output = 0  # Only one element, so no difference
        assert max_Abs_Diff(arr) == expected_output

    def test_multiple_spaces_5(self):
        arr = []
        expected_output = 0  # Empty list should return 0
        assert max_Abs_Diff(arr) == expected_output

    def test_multiple_spaces_6(self):
        arr = [5, -5, 10, -10]
        expected_output = 20  # Max absolute difference is between -10 and 10
        assert max_Abs_Diff(arr) == expected_output

    def test_multiple_spaces_7(self):
        arr = [1, 2, 2, 1]
        expected_output = 1  # Duplicates present, max difference is between 1 and 2
        assert max_Abs_Diff(arr) == expected_output

