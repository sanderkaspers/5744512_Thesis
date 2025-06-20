import unittest
from datasets.GPT_4.Zero_shot.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        lst = [1, 2, 2, 3, 3, 3]
        expected_output = 3  # 3 occurs the most times
        assert max_occurrences(lst) == expected_output

    def test_multiple_spaces_2(self):
        lst = [1, 2, 3]
        expected_output = 1  # All elements are unique, return any of them
        assert max_occurrences(lst) in lst

    def test_multiple_spaces_3(self):
        lst = [1, 2, 2, 3, 3]
        expected_output = 2  # Both 2 and 3 have the same frequency, function may return either
        assert max_occurrences(lst) in [2, 3]

    def test_multiple_spaces_4(self):
        lst = []
        expected_output = None  # Empty list, depending on the implementation
        assert max_occurrences(lst) == expected_output

    def test_multiple_spaces_5(self):
        lst = [42]
        expected_output = 42  # Single element list, should return that element
        assert max_occurrences(lst) == expected_output

    def test_multiple_spaces_6(self):
        lst = ["a", "b", "b", "a", "c", "c", "c"]
        expected_output = "c"  # Mixed data types with strings, "c" occurs most often
        assert max_occurrences(lst) == expected_output

    def test_multiple_spaces_7(self):
        lst = [-1, -2, -2, -1, -3, -3, -3]
        expected_output = -3  # Negative numbers, -3 occurs most often
        assert max_occurrences(lst) == expected_output

