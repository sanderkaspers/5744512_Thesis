import unittest
from datasets.GPT_4.Zero_shot.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        a = 2
        b = 3
        expected_output = 8
        assert power(a, b) == expected_output

    def test_multiple_spaces_2(self):
        a = 5
        b = 0
        expected_output = 1
        assert power(a, b) == expected_output

    def test_multiple_spaces_3(self):
        a = 0
        b = 3
        expected_output = 0
        assert power(a, b) == expected_output

    def test_multiple_spaces_4(self):
        a = 0
        b = 0
        expected_output = 1
        assert power(a, b) == expected_output

    def test_multiple_spaces_5(self):
        a = -2
        b = 3
        expected_output = -8
        assert power(a, b) == expected_output

    def test_multiple_spaces_6(self):
        a = -2
        b = 4
        expected_output = 16
        assert power(a, b) == expected_output

    def test_multiple_spaces_7(self):
        a = 2
        b = -2
        try:
            power(a, b)
            expected_output = 0.25
        except RecursionError:
            expected_output = "RecursionError"
        assert expected_output == "RecursionError"

    def test_multiple_spaces_8(self):
        a = 2.5
        b = 3
        expected_output = 15.625
        assert power(a, b) == expected_output

