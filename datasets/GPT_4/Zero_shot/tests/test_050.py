import unittest
from datasets.GPT_4.Zero_shot.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        word = "hello_world"
        expected_output = "HelloWorld"
        assert snake_to_camel(word) == expected_output

    def test_multiple_spaces_2(self):
        word = "python"
        expected_output = "Python"
        assert snake_to_camel(word) == expected_output

    def test_multiple_spaces_3(self):
        word = "this_is_a_test"
        expected_output = "ThisIsATest"
        assert snake_to_camel(word) == expected_output

    def test_multiple_spaces_4(self):
        word = "consecutive__underscores"
        expected_output = "ConsecutiveUnderscores"
        assert snake_to_camel(word) == expected_output

    def test_multiple_spaces_5(self):
        word = "_leading_and_trailing_"
        expected_output = "LeadingAndTrailing"
        assert snake_to_camel(word) == expected_output

    def test_multiple_spaces_6(self):
        word = "version_2_point_0"
        expected_output = "Version2Point0"
        assert snake_to_camel(word) == expected_output

    def test_empty_string(self):
        word = ""
        expected_output = ""
        assert snake_to_camel(word) == expected_output

    def test_multiple_spaces_7(self):
        word = "mixED_case_STRING"
        expected_output = "MixedCaseString"
        assert snake_to_camel(word) == expected_output

