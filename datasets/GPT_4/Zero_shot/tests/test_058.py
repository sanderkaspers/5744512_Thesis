import unittest
from datasets.GPT_4.Zero_shot.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        text = "123"
        expected_output = True
        assert check_integer(text) == expected_output

    def test_multiple_spaces_2(self):
        text = "-123"
        expected_output = True
        assert check_integer(text) == expected_output

    def test_multiple_spaces_3(self):
        text = "   123   "
        expected_output = True
        assert check_integer(text) == expected_output

    def test_multiple_spaces_4(self):
        text = "abc"
        expected_output = False
        assert check_integer(text) == expected_output

    def test_empty_string(self):
        text = ""
        expected_output = False
        assert check_integer(text) == expected_output

    def test_multiple_spaces_5(self):
        text = "123abc"
        expected_output = False
        assert check_integer(text) == expected_output

    def test_multiple_spaces_6(self):
        text = "+123"
        expected_output = True
        assert check_integer(text) == expected_output

