import unittest
from datasets.GPT_4.Zero_shot.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        s = "123"
        expected_output = 2
        assert count_Substrings(s) == expected_output

    def test_multiple_spaces_2(self):
        s = "0000"
        expected_output = 10
        assert count_Substrings(s) == expected_output

    def test_multiple_spaces_3(self):
        s = "5"
        expected_output = 1
        assert count_Substrings(s) == expected_output

    def test_multiple_spaces_4(self):
        s = "1234"
        expected_output = 3
        assert count_Substrings(s) == expected_output

    def test_multiple_spaces_5(self):
        s = "4321"
        expected_output = 3
        assert count_Substrings(s) == expected_output

    def test_empty_string(self):
        s = ""
        expected_output = 0
        assert count_Substrings(s) == expected_output

    def test_multiple_spaces_6(self):
        s = "11111"
        expected_output = 5
        assert count_Substrings(s) == expected_output

