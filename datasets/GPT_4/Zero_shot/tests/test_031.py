import unittest
from datasets.GPT_4.Zero_shot.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        strr = "abc"
        expected_output = 'f'
        assert get_Char(strr) == expected_output

    def test_multiple_spaces_2(self):
        strr = "zzzz"
        expected_output = 'z'
        assert get_Char(strr) == expected_output

    def test_multiple_spaces_3(self):
        strr = "a"
        expected_output = 'a'
        assert get_Char(strr) == expected_output

    def test_multiple_spaces_4(self):
        strr = "abcdefghijklmnopqrstuvwxyz"
        expected_output = 'l'
        assert get_Char(strr) == expected_output

    def test_empty_string(self):
        strr = ""
        expected_output = 'z'
        assert get_Char(strr) == expected_output

    def test_multiple_spaces_5(self):
        strr = "cccc"
        expected_output = 'p'
        assert get_Char(strr) == expected_output

    def test_multiple_spaces_6(self):
        strr = "aaa"
        expected_output = 'c'
        assert get_Char(strr) == expected_output

