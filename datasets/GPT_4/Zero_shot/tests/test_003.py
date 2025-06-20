import unittest
from datasets.GPT_4.Zero_shot.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        l = 10
        b = 5
        h = 6
        expected_output = 150.0
        assert find_Volume(l, b, h) == expected_output

    def test_multiple_spaces_2(self):
        l = 0
        b = 5
        h = 6
        expected_output = 0.0
        assert find_Volume(l, b, h) == expected_output

    def test_multiple_spaces_3(self):
        l = 0
        b = 0
        h = 0
        expected_output = 0.0
        assert find_Volume(l, b, h) == expected_output

    def test_multiple_spaces_4(self):
        l = -10
        b = 5
        h = 6
        expected_output = -150.0
        assert find_Volume(l, b, h) == expected_output

    def test_multiple_spaces_5(self):
        l = 10.5
        b = 5.2
        h = 6.3
        expected_output = 171.675
        assert find_Volume(l, b, h) == expected_output

    def test_multiple_spaces_6(self):
        l = 10000
        b = 5000
        h = 6000
        expected_output = 150000000000.0
        assert find_Volume(l, b, h) == expected_output

