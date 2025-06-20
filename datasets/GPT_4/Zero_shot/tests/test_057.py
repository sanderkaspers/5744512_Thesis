import unittest
from datasets.GPT_4.Zero_shot.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        nestedlist = [[1, 2, 3], [2, 3, 4], [2, 5, 3]]
        expected_output = [2, 3]  # 2 and 3 are common across all sublists
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_2(self):
        nestedlist = [[1, 2], [3, 4], [5, 6]]
        expected_output = []  # No common elements
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_3(self):
        nestedlist = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
        expected_output = [3]  # Only 3 is common
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_4(self):
        nestedlist = [[1, 2, 3], [], [2, 3, 4]]
        expected_output = []  # An empty sublist results in no common elements
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_5(self):
        nestedlist = [[1, 2, 3]]
        expected_output = [1, 2, 3]  # Only one sublist, so all elements are common
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_6(self):
        nestedlist = [[1, 2], [1, 2], [1, 2]]
        expected_output = [1, 2]  # All sublists are identical
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_7(self):
        nestedlist = [[1, 2, 3], [2], [2, 3]]
        expected_output = [2]  # 2 is the only common element
        assert common_in_nested_lists(nestedlist) == expected_output

    def test_multiple_spaces_8(self):
        nestedlist = [[1, "a", 3.0], ["a", 4, 3.0], [5, "a", 3.0]]
        expected_output = ["a", 3.0]  # "a" and 3.0 are common across all sublists
        assert common_in_nested_lists(nestedlist) == expected_output

