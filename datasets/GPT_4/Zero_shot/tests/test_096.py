import unittest
from datasets.GPT_4.Zero_shot.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        s = "abracadabra"
        expected_output = 5  # 'a' appears 5 times in the string
        assert count_occurance(s) == expected_output

    def test_multiple_spaces_2(self):
        s = "hello world"
        expected_output = 0  # No 'a' in the string
        assert count_occurance(s) == expected_output

    def test_multiple_spaces_3(self):
        s = "aaaaa"
        expected_output = 5  # String composed entirely of 'a'
        assert count_occurance(s) == expected_output

    def test_empty_string(self):
        s = ""
        expected_output = 0  # Empty string should return 0
        assert count_occurance(s) == expected_output

    def test_multiple_spaces_4(self):
        s = "Aardvark"
        expected_output = 2  # Case-sensitive count, only lowercase 'a' is counted
        assert count_occurance(s) == expected_output

    def test_multiple_spaces_5(self):
        s = "a!@#$%^&*a"
        expected_output = 2  # String with special characters, 'a' appears 2 times
        assert count_occurance(s) == expected_output

    def test_multiple_spaces_6(self):
        s = "a" * 10000 + "b" * 10000
        expected_output = 10000  # Large string with 10000 'a's
        assert count_occurance(s) == expected_output

