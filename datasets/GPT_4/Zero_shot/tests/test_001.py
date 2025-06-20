import unittest
from datasets.GPT_4.Zero_shot.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        s = "hello world"
        ch = "o"
        expected_output = "hell wrld"
        assert remove_Occ(s, ch) == expected_output

    def test_multiple_spaces_2(self):
        s = "hello"
        ch = "h"
        expected_output = "ello"
        assert remove_Occ(s, ch) == expected_output

    def test_multiple_spaces_3(self):
        s = "hello"
        ch = "x"
        expected_output = "hello"
        assert remove_Occ(s, ch) == expected_output

    def test_empty_string(self):
        s = ""
        ch = "a"
        expected_output = ""
        assert remove_Occ(s, ch) == expected_output

    def test_empty_string_2(self):
        s = "a"
        ch = "a"
        expected_output = ""
        assert remove_Occ(s, ch) == expected_output

    def test_multiple_spaces_4(self):
        s = "@hello@world@"
        ch = "@"
        expected_output = "hello@world"
        assert remove_Occ(s, ch) == expected_output

    def test_single_space(self):
        s = "a b c d"
        ch = " "
        expected_output = "abc d"
        assert remove_Occ(s, ch) == expected_output

    def test_multiple_spaces_5(self):
        s = "aaaaaa"
        ch = "a"
        expected_output = "aaaa"
        assert remove_Occ(s, ch) == expected_output

