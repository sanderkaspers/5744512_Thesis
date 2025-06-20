import unittest
from datasets.GPT_4.Zero_shot.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        s = "This is a test"
        expected_output = True
        assert word_len(s) == expected_output

    def test_multiple_spaces_2(self):
        s = "This is cool"
        expected_output = False
        assert word_len(s) == expected_output

    def test_multiple_spaces_3(self):
        s = "Python"
        expected_output = True
        assert word_len(s) == expected_output

    def test_multiple_spaces_4(self):
        s = "Code"
        expected_output = False
        assert word_len(s) == expected_output

    def test_empty_string(self):
        s = ""
        expected_output = False
        assert word_len(s) == expected_output

    def test_multiple_spaces_5(self):
        s = "I am odd"
        expected_output = True
        assert word_len(s) == expected_output

    def test_multiple_spaces_6(self):
        s = "Hello, world!"
        expected_output = True
        assert word_len(s) == expected_output

    def test_multiple_spaces_7(self):
        s = "This  is  spaced out"
        expected_output = True
        assert word_len(s) == expected_output

