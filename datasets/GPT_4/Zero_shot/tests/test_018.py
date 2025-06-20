import unittest
from datasets.GPT_4.Zero_shot.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list = [1, -2, 3, -4, 5, 0]
        expected_output = 4
        assert pos_count(list) == expected_output

    def test_write_all_the__cases_for_this(self):
        list = [10, 20, 30, 40]
        expected_output = 4
        assert pos_count(list) == expected_output

    def test_multiple_spaces_3(self):
        list = [-10, -20, -30, -40]
        expected_output = 0
        assert pos_count(list) == expected_output

    def test_multiple_spaces_4(self):
        list = [5]
        expected_output = 1
        assert pos_count(list) == expected_output

    def test_multiple_spaces_5(self):
        list = [-5]
        expected_output = 0
        assert pos_count(list) == expected_output

    def test_write_all_the__cases_for_this_1(self):
        list = [0, 0, 0]
        expected_output = 3
        assert pos_count(list) == expected_output

    def test_multiple_spaces_7(self):
        list = [1.5, -2.3, 3.7, 0.0]
        expected_output = 3
        assert pos_count(list) == expected_output

    def test_multiple_spaces_8(self):
        list = []
        expected_output = 0
        assert pos_count(list) == expected_output

