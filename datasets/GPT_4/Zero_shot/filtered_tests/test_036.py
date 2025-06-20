import unittest
from datasets.GPT_4.Zero_shot.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [1, 2, 2, 3, 3, 3]
        expected_output = {1: 1, 2: 2, 3: 3}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [4, 4, 4, 4]
        expected_output = {4: 4}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [5, 6, 7, 8]
        expected_output = {5: 1, 6: 1, 7: 1, 8: 1}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_4(self):
        list1 = []
        expected_output = {}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_5(self):
        list1 = [1, "apple", 1, "banana", "apple"]
        expected_output = {1: 2, "apple": 2, "banana": 1}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_6(self):
        list1 = [-1, -2, -1, -3, -2, -2]
        expected_output = {-1: 2, -2: 3, -3: 1}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_7(self):
        list1 = ["@", "@", "#", "!"]
        expected_output = {"@": 2, "#": 1, "!": 1}
        assert freq_count(list1) == expected_output

    def test_multiple_spaces_8(self):
        list1 = [42]
        expected_output = {42: 1}
        assert freq_count(list1) == expected_output

