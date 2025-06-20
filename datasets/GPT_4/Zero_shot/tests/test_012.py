import unittest
from datasets.GPT_4.Zero_shot.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 1
        expected_output = 1
        assert is_octagonal(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 2
        expected_output = 10
        assert is_octagonal(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 3
        expected_output = 27
        assert is_octagonal(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 4
        expected_output = 52
        assert is_octagonal(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 10
        expected_output = 226
        assert is_octagonal(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 0
        expected_output = 0
        assert is_octagonal(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 1000
        expected_output = 2998000
        assert is_octagonal(n) == expected_output

