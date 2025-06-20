import unittest
from datasets.GPT_4.Zero_shot.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        string = "hello"
        expected_output = ['h', 'e', 'l', 'l', 'o']
        assert string_to_list(string) == expected_output

    def test_empty_string(self):
        string = ""
        expected_output = []
        assert string_to_list(string) == expected_output

    def test_single_space(self):
        string = "a b\tc\nd"
        expected_output = ['a', ' ', 'b', '\t', 'c', '\n', 'd']
        assert string_to_list(string) == expected_output

    def test_multiple_spaces_2(self):
        string = "hello!"
        expected_output = ['h', 'e', 'l', 'l', 'o', '!']
        assert string_to_list(string) == expected_output

    def test_multiple_spaces_3(self):
        string = "こんにちは"
        expected_output = ['こ', 'ん', 'に', 'ち', 'は']
        assert string_to_list(string) == expected_output

    def test_multiple_spaces_4(self):
        string = "😊"
        expected_output = ['😊']
        assert string_to_list(string) == expected_output

    def test_multiple_spaces_5(self):
        string = "Z"
        expected_output = ['Z']
        assert string_to_list(string) == expected_output

