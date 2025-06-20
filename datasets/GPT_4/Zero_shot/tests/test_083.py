import unittest
from datasets.GPT_4.Zero_shot.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        Input = [1, 2, [3, 4], 5]
        expected_output = [[3, 4]]  # A single list within the main list
        assert find_lists(Input) == expected_output

    def test_multiple_spaces_2(self):
        Input = [1, [2, [3, 4]], 5]
        expected_output = [[2, [3, 4]], [3, 4]]  # Nested lists
        assert find_lists(Input) == expected_output

    def test_multiple_spaces_3(self):
        Input = []
        expected_output = []  # Empty list as input should return an empty list
        assert find_lists(Input) == expected_output

    def test_multiple_spaces_4(self):
        Input = [1, 2, 3, 4]
        expected_output = []  # No lists in input
        assert find_lists(Input) == expected_output

    def test_multiple_spaces_5(self):
        Input = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[1, 2], [3, 4], [5, 6]]  # The entire input is a list of lists
        assert find_lists(Input) == expected_output

    def test_multiple_spaces_6(self):
        Input = "This is not a list"
        expected_output = []  # Input is not a list, so should return an empty list
        assert find_lists(Input) == expected_output

    def test_multiple_spaces_7(self):
        Input = [1, [2, 3], 4, [5, [6, 7]], 8]
        expected_output = [[2, 3], [5, [6, 7]], [6, 7]]  # Multiple lists at various depths
        assert find_lists(Input) == expected_output

