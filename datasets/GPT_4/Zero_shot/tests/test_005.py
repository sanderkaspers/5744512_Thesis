import unittest
from datasets.GPT_4.Zero_shot.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        a = 5
        expected_output = 20
        assert square_perimeter(a) == expected_output

    def test_multiple_spaces_2(self):
        a = 0
        expected_output = 0
        assert square_perimeter(a) == expected_output

    def test_multiple_spaces_3(self):
        a = -5
        expected_output = -20
        assert square_perimeter(a) == expected_output

    def test_multiple_spaces_4(self):
        a = 4.5
        expected_output = 18.0
        assert square_perimeter(a) == expected_output

    def test_multiple_spaces_5(self):
        a = 1000000
        expected_output = 4000000
        assert square_perimeter(a) == expected_output

