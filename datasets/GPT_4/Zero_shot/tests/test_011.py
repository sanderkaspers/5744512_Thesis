import unittest
from datasets.GPT_4.Zero_shot.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        x = 5
        y = -3
        expected_output = True
        assert opposite_Signs(x, y) == expected_output

    def test_multiple_spaces_2(self):
        x = 7
        y = 2
        expected_output = False
        assert opposite_Signs(x, y) == expected_output

    def test_multiple_spaces_3(self):
        x = -4
        y = -9
        expected_output = False
        assert opposite_Signs(x, y) == expected_output

    def test_multiple_spaces_4(self):
        x = 0
        y = 10
        expected_output = False
        assert opposite_Signs(x, y) == expected_output

    def test_multiple_spaces_5(self):
        x = -5
        y = 0
        expected_output = False
        assert opposite_Signs(x, y) == expected_output

    def test_multiple_spaces_6(self):
        x = 123456789
        y = -987654321
        expected_output = True
        assert opposite_Signs(x, y) == expected_output

    def test_multiple_spaces_7(self):
        x = 0
        y = 0
        expected_output = False
        assert opposite_Signs(x, y) == expected_output

