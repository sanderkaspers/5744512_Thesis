import unittest
from datasets.GPT_4.Zero_shot.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 0
        expected_output = 1
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 1
        expected_output = 1
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 2
        expected_output = 7
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 3
        expected_output = 19
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 5
        expected_output = 61
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 10
        expected_output = 271
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 100
        expected_output = 29701
        assert centered_hexagonal_number(n) == expected_output

    def test_multiple_spaces_8(self):
        n = -1
        try:
            centered_hexagonal_number(n)
            expected_output = None
        except ValueError:
            expected_output = "ValueError"
        assert expected_output == "ValueError"

