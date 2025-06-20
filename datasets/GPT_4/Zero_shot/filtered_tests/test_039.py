import unittest
from datasets.GPT_4.Zero_shot.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        str1 = ["hello", "world", "python"]
        sub_str = "wor"
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_2(self):
        str1 = ["hello", "world", "python"]
        sub_str = "java"
        expected_output = False
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_3(self):
        str1 = []
        sub_str = "test"
        expected_output = False
        assert find_substring(str1, sub_str) == expected_output

    def test_empty_string(self):
        str1 = ["hello", "world"]
        sub_str = ""
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_4(self):
        str1 = ["apple", "banana", "cherry"]
        sub_str = "banana"
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_5(self):
        str1 = ["apple", "banana", "cherry"]
        sub_str = "ban"
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_6(self):
        str1 = ["test", "test", "test"]
        sub_str = "est"
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_7(self):
        str1 = ["hello!", "world$", "@python"]
        sub_str = "@py"
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

    def test_multiple_spaces_8(self):
        str1 = ["apple", "banana", "cherry"]
        sub_str = "rry"
        expected_output = True
        assert find_substring(str1, sub_str) == expected_output

