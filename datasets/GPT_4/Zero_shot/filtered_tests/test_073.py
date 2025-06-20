import unittest
from datasets.GPT_4.Zero_shot.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        str1 = "hello"
        expected_output = "holle"  # The vowels e and o are reversed
        assert reverse_vowels(str1) == expected_output

    def test_multiple_spaces_2(self):
        str1 = "bcdfg"
        expected_output = "bcdfg"  # No vowels to reverse
        assert reverse_vowels(str1) == expected_output

    def test_multiple_spaces_3(self):
        str1 = "aeiou"
        expected_output = "uoiea"  # All vowels reversed
        assert reverse_vowels(str1) == expected_output

    def test_multiple_spaces_4(self):
        str1 = "a"
        expected_output = "a"  # Single vowel, no change
        assert reverse_vowels(str1) == expected_output

    def test_empty_string(self):
        str1 = ""
        expected_output = ""  # Empty string should return an empty string
        assert reverse_vowels(str1) == expected_output

    def test_multiple_spaces_5(self):
        str1 = "hEllo"
        expected_output = "hollE"  # Mix of uppercase and lowercase vowels
        assert reverse_vowels(str1) == expected_output

    def test_multiple_spaces_6(self):
        str1 = "h@ell!o"
        expected_output = "h@oll!e"  # Vowels reversed with special characters remaining in place
        assert reverse_vowels(str1) == expected_output

