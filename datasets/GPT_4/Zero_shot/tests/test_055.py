import unittest
from datasets.GPT_4.Zero_shot.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        expected_output = [1, 2, 3, 4, 5, 6]
        assert list(merge_sorted_list(num1, num2)) == expected_output

    def test_multiple_spaces_2(self):
        num1 = []
        num2 = [1, 2, 3]
        expected_output = [1, 2, 3]
        assert list(merge_sorted_list(num1, num2)) == expected_output

    def test_multiple_spaces_3(self):
        num1 = []
        num2 = []
        expected_output = []
        assert list(merge_sorted_list(num1, num2)) == expected_output

    def test_multiple_spaces_4(self):
        num1 = [-3, -2, -1]
        num2 = [-6, -4, -2]
        expected_output = [-6, -4, -3, -2, -2, -1]
        assert list(merge_sorted_list(num1, num2)) == expected_output

    def test_multiple_spaces_5(self):
        num1 = [1, 2.5, 3.5]
        num2 = [2, 4.5, 6]
        expected_output = [1, 2, 2.5, 3.5, 4.5, 6]
        assert list(merge_sorted_list(num1, num2)) == expected_output

    def test_multiple_spaces_6(self):
        num1 = [1, 2, 3]
        num2 = [1, 2, 3]
        expected_output = [1, 1, 2, 2, 3, 3]
        assert list(merge_sorted_list(num1, num2)) == expected_output

    def test_multiple_spaces_7(self):
        num1 = [10]
        num2 = [5]
        expected_output = [5, 10]
        assert list(merge_sorted_list(num1, num2)) == expected_output

