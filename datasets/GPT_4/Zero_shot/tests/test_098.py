import unittest
from datasets.GPT_4.Zero_shot.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        arr = [1, 2, 2, 2, 3]
        n = 5
        x = 2
        expected_output = True  # x is the majority element (appears 3 out of 5 times)
        assert is_majority(arr, n, x) == expected_output

    def test_multiple_spaces_2(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        x = 6
        expected_output = False  # x is not in the array
        assert is_majority(arr, n, x) == expected_output

    def test_multiple_spaces_3(self):
        arr = [1, 2, 3, 3, 4]
        n = 5
        x = 3
        expected_output = False  # x is present but not a majority
        assert is_majority(arr, n, x) == expected_output

    def test_multiple_spaces_4(self):
        arr = [3]
        n = 1
        x = 3
        expected_output = True  # Single element array with x as the only element
        assert is_majority(arr, n, x) == expected_output

    def test_multiple_spaces_5(self):
        arr = []
        n = 0
        x = 3
        expected_output = False  # Empty array should return False
        assert is_majority(arr, n, x) == expected_output

    def test_multiple_spaces_6(self):
        arr = [2, 2, 2, 2]
        n = 4
        x = 2
        expected_output = True  # All elements are x, so x is the majority
        assert is_majority(arr, n, x) == expected_output

    def test_multiple_spaces_7(self):
        arr = [1] * 10000 + [2] * 5000
        n = 15000
        x = 1
        expected_output = True  # Large array with x as the majority element
        assert is_majority(arr, n, x) == expected_output

