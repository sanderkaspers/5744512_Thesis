import unittest
from datasets.GPT_4.Zero_shot.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 3
        str = "The quick brown fox"
        expected_output = ["quick", "brown"]
        assert long_words(n, str) == expected_output

    def test_multiple_spaces_2(self):
        n = 5
        str = "cat dog mouse"
        expected_output = ["mouse"]  # Only "mouse" is longer than 5 characters
        assert long_words(n, str) == expected_output

    def test_multiple_spaces_3(self):
        n = 3
        str = "a b c"
        expected_output = []  # No words longer than 3 characters
        assert long_words(n, str) == expected_output

    def test_empty_string(self):
        n = 3
        str = ""
        expected_output = []  # Empty string should return an empty list
        assert long_words(n, str) == expected_output

    def test_multiple_spaces_4(self):
        n = 4
        str = "well-done"
        expected_output = ["well-done"]  # Handle hyphenated words as single words
        assert long_words(n, str) == expected_output

    def test_multiple_spaces_5(self):
        n = 0
        str = "one two three four"
        expected_output = ["one", "two", "three", "four"]  # All words should be returned
        assert long_words(n, str) == expected_output

    def test_multiple_spaces_6(self):
        n = 10
        str = "small medium large"
        expected_output = []  # No words longer than 10 characters
        assert long_words(n, str) == expected_output

