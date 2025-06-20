import unittest
from datasets.GPT_4.Few_shot.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        string = "hello world"
        second_string = "ole"
        expected_output = "h wrld"
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_2(self):
        string = "hello"
        second_string = "xyz"
        expected_output = "hello"
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_3(self):
        string = ""
        second_string = "abc"
        expected_output = ""
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_4(self):
        string = "hello"
        second_string = ""
        expected_output = "hello"
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_5(self):
        string = ""
        second_string = ""
        expected_output = ""
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_6(self):
        string = "abcdef"
        second_string = "abcdef"
        expected_output = ""
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_7(self):
        string = "Hello World"
        second_string = "h"
        expected_output = "Hello World"
        assert remove_dirty_chars(string, second_string) == expected_output

    def test_case_8(self):
        string = "hello@world!"
        second_string = "@!"
        expected_output = "helloworld"
        assert remove_dirty_chars(string, second_string) == expected_output

