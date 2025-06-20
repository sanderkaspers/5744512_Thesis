import unittest
from datasets.GPT_4.Zero_shot.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 12
        expected_output = False
        assert check(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 5
        expected_output = False
        assert check(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 11
        expected_output = False
        assert check(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 37
        expected_output = False
        assert check(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 120
        expected_output = False
        assert check(n) == expected_output

    def test_multiple_spaces_6(self):
        n = -12
        expected_output = False
        assert check(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 13
        expected_output = False
        assert check(n) == expected_output

