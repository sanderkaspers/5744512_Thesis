import unittest
from datasets.GPT_4.Zero_shot.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        text = "abc_def"
        expected_output = True
        assert text_lowercase_underscore(text) == expected_output

    def test_multiple_spaces_2(self):
        text = "abcdef"
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

    def test_multiple_spaces_3(self):
        text = "Abc_Def"
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

    def test_multiple_spaces_4(self):
        text = "abc_def_ghi"
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

    def test_multiple_spaces_5(self):
        text = "abc_123"
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

    def test_multiple_spaces_6(self):
        text = "abc_@def"
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

    def test_empty_string(self):
        text = ""
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

    def test_multiple_spaces_7(self):
        text = "abc_def test_multiple_spaces_7(self) == expected_output"

    def test_multiple_spaces_8(self):
        text = "abc_"
        expected_output = False
        assert text_lowercase_underscore(text) == expected_output

