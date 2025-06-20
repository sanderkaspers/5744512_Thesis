import unittest
from datasets.GPT_4.Zero_shot.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        test_list = [(1, 5), (2, 8), (-3, 4)]
        expected_output = 7
        assert max_difference(test_list) == expected_output

    def test_multiple_spaces_2(self):
        test_list = [(10, 20), (30, 40), (5, 15)]
        expected_output = 10
        assert max_difference(test_list) == expected_output

    def test_write_all_the__cases_for_this__to_find(self):
        test_list = [(10, 50)]
        expected_output = 40
        assert max_difference(test_list) == expected_output

    def test_multiple_spaces_4(self):
        test_list = [(7, 7), (3, 3)]
        expected_output = 0
        assert max_difference(test_list) == expected_output

    def test_multiple_spaces_5(self):
        test_list = []
        try:
            max_difference(test_list)
            expected_output = None
        except ValueError:
            expected_output = "ValueError"
        assert expected_output == "ValueError"

    def test_multiple_spaces_6(self):
        test_list = [(0, 0), (0, 5), (10, 0)]
        expected_output = 10
        assert max_difference(test_list) == expected_output

    def test_multiple_spaces_7(self):
        test_list = [(10, 20), (15, 25), (30, 40)]
        expected_output = 10
        assert max_difference(test_list) == expected_output

