import unittest
from datasets.GPT_4.Zero_shot.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 4]
        expected_output = [1, 3, 5]  # Elements 2 and 4 should be removed
        assert remove_elements(list1, list2) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        expected_output = [1, 2, 3]  # No common elements, so list1 remains unchanged
        assert remove_elements(list1, list2) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        expected_output = []  # All elements are removed
        assert remove_elements(list1, list2) == expected_output

    def test_multiple_spaces_4(self):
        list1 = [1, 2, 3]
        list2 = []
        expected_output = [1, 2, 3]  # list2 is empty, so no elements should be removed
        assert remove_elements(list1, list2) == expected_output

    def test_multiple_spaces_5(self):
        list1 = []
        list2 = [1, 2, 3]
        expected_output = []  # list1 is empty, so the result should be empty
        assert remove_elements(list1, list2) == expected_output

    def test_multiple_spaces_6(self):
        list1 = [1, 2, 2, 3, 4]
        list2 = [2]
        expected_output = [1, 3, 4]  # All occurrences of 2 should be removed
        assert remove_elements(list1, list2) == expected_output

    def test_multiple_spaces_7(self):
        list1 = ["a", 1, "b", 2]
        list2 = [1, "b"]
        expected_output = ["a", 2]  # Elements with different data types should be removed
        assert remove_elements(list1, list2) == expected_output

