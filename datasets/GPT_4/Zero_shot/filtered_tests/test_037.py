import unittest
from datasets.GPT_4.Zero_shot.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        N = 10
        expected_output = 9
        assert closest_num(N) == expected_output

    def test_multiple_spaces_2(self):
        N = 1
        expected_output = 0
        assert closest_num(N) == expected_output

    def test_multiple_spaces_3(self):
        N = 0
        expected_output = -1
        assert closest_num(N) == expected_output

    def test_multiple_spaces_4(self):
        N = -5
        expected_output = -6
        assert closest_num(N) == expected_output

    def test_multiple_spaces_5(self):
        N = 1000000
        expected_output = 999999
        assert closest_num(N) == expected_output

    def test_multiple_spaces_6(self):
        N = 10.5
        expected_output = 9.5
        assert closest_num(N) == expected_output

