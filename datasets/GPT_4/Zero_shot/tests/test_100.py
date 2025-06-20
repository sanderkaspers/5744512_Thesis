import unittest
from datasets.GPT_4.Zero_shot.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_empty_string(self):
        str_input = ""
        expected_output = ""
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces(self):
        str_input = "a"
        expected_output = "a"
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces_2(self):
        str_input = "abcd"  # Even-length string
        expected_output = "ac"
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces_3(self):
        str_input = "abcde"  # Odd-length string
        expected_output = "ace"
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces_4(self):
        str_input = "aaaa"  # All identical characters
        expected_output = "aa"
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces_5(self):
        str_input = "a1!b2@c3#"  # Special characters
        expected_output = "a!b@c#"
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces_6(self):
        str_input = "Hello\nWorld"  # Multi-line string
        expected_output = "Hlo\nWrd"
        assert odd_values_string(str_input) == expected_output

    def test_multiple_spaces_7(self):
        str_input = "The quick brown fox jumps"  # Longer string
        expected_output = "Teqikbonfxjms"
        assert odd_values_string(str_input) == expected_output

