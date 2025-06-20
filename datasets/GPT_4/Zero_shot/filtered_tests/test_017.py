import unittest
from datasets.GPT_4.Zero_shot.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this__to_flat(self):
        data_list = [1, 2, [3, 4], [5, 6], 7]
        expected_output = 28
        assert recursive_list_sum(data_list) == expected_output

    def test_multiple_spaces_2(self):
        data_list = [1, [2, [3, [4, [5]]]]]
        expected_output = 15
        assert recursive_list_sum(data_list) == expected_output

    def test_multiple_spaces_3(self):
        data_list = []
        expected_output = 0
        assert recursive_list_sum(data_list) == expected_output

    def test_write_all_the__cases_for_this__to_flat_1(self):
        data_list = [5]
        expected_output = 5
        assert recursive_list_sum(data_list) == expected_output

    def test_multiple_spaces_5(self):
        data_list = [1, [], [2, []], 3]
        expected_output = 6
        assert recursive_list_sum(data_list) == expected_output

    def test_multiple_spaces_6(self):
        data_list = [1, 2, [3.5, 4], ['a', 6], 7]
        try:
            recursive_list_sum(data_list)
            expected_output = None
        except TypeError:
            expected_output = "TypeError"
        assert expected_output == "TypeError"

    def test_multiple_spaces_7(self):
        data_list = [1, 2, 3, 4, 5]
        expected_output = 15
        assert recursive_list_sum(data_list) == expected_output

