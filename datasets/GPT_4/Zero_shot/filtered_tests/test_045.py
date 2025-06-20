import unittest
from datasets.GPT_4.Zero_shot.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [[1, 2, 2], [3, 3, 3], [4, 4]]
        expected_output = {1: 1, 2: 2, 3: 3, 4: 2}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [[5, 5, 5], [5, 5], [5]]
        expected_output = {5: 6}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [[6], [7], [8], [9]]
        expected_output = {6: 1, 7: 1, 8: 1, 9: 1}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_4(self):
        list1 = []
        expected_output = {}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_5(self):
        list1 = [[10, 11], [], [12, 12, 12], []]
        expected_output = {10: 1, 11: 1, 12: 3}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_6(self):
        list1 = [[13, "apple", 13], ["banana", "apple"], [None, 13]]
        expected_output = {13: 3, "apple": 2, "banana": 1, None: 1}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_7(self):
        list1 = [[-1, -2, -2], [-3, -3, -1], [-2]]
        expected_output = {-1: 2, -2: 3, -3: 2}
        assert frequency_lists(list1) == expected_output

    def test_multiple_spaces_8(self):
        list1 = [["@", "@", "#"], ["$", "#", "@"]]
        expected_output = {"@": 3, "#": 2, "$": 1}
        assert frequency_lists(list1) == expected_output

