import unittest
from datasets.GPT_4.Zero_shot.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        test_list = [1, 2, 2, 3, 4, 4, 5]
        expected_output = [1, 3, 5]  # Only these elements appear once
        assert extract_singly(test_list) == expected_output

    def test_multiple_spaces_2(self):
        test_list = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]  # All elements are unique
        assert extract_singly(test_list) == expected_output

    def test_multiple_spaces_3(self):
        test_list = [1, 1, 2, 2, 3, 3]
        expected_output = []  # All elements are duplicates
        assert extract_singly(test_list) == expected_output

    def test_multiple_spaces_4(self):
        test_list = []
        expected_output = []  # Empty list should return an empty list
        assert extract_singly(test_list) == expected_output

    def test_multiple_spaces_5(self):
        test_list = [7]
        expected_output = [7]  # Single element list should return that element
        assert extract_singly(test_list) == expected_output

    def test_multiple_spaces_6(self):
        test_list = [1, "a", "b", "a", 2, 2]
        expected_output = [1, "b"]  # Mixed data types with unique and duplicate elements
        assert extract_singly(test_list) == expected_output

    def test_multiple_spaces_7(self):
        test_list = [i for i in range(1000)] + [i for i in range(1000)]
        expected_output = []  # Large list with all elements duplicated
        assert extract_singly(test_list) == expected_output

