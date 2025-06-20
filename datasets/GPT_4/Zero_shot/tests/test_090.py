import unittest
from datasets.GPT_4.Zero_shot.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        str1 = "abc"
        expected_output = {'a': [0], 'b': [1], 'c': [2]}  # Basic case with unique characters
        assert count_char_position(str1) == expected_output

    def test_multiple_spaces_2(self):
        str1 = "aabbc"
        expected_output = {'a': [0, 1], 'b': [2, 3], 'c': [4]}  # Repeated characters
        assert count_char_position(str1) == expected_output

    def test_empty_string(self):
        str1 = ""
        expected_output = {}  # Empty string should return an empty dictionary
        assert count_char_position(str1) == expected_output

    def test_single_space(self):
        str1 = "a b c"
        expected_output = {'a': [0], ' ': [1, 3], 'b': [2], 'c': [4]}  # String with spaces
        assert count_char_position(str1) == expected_output

    def test_multiple_spaces_3(self):
        str1 = "a!b@c#"
        expected_output = {'a': [0], '!': [1], 'b': [2], '@': [3], 'c': [4], '#': [5]}  # Special characters
        assert count_char_position(str1) == expected_output

    def test_multiple_spaces_4(self):
        str1 = "AaBbCc"
        expected_output = {'A': [0], 'a': [1], 'B': [2], 'b': [3], 'C': [4], 'c': [5]}  # Case sensitivity check
        assert count_char_position(str1) == expected_output

    def test_multiple_spaces_5(self):
        str1 = "こんにちは"
        expected_output = {'こ': [0], 'ん': [1], 'に': [2], 'ち': [3], 'は': [4]}  # Unicode characters
        assert count_char_position(str1) == expected_output

