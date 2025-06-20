import unittest
from datasets.GPT_4.Zero_shot.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this__to_sort(self):
        nums = [34, 7, 23, 32, 5, 62]
        expected_output = [5, 7, 23, 32, 34, 62]
        assert comb_sort(nums) == expected_output

    def test_multiple_spaces_2(self):
        nums = []
        expected_output = []
        assert comb_sort(nums) == expected_output

    def test_write_all_the__cases_for_this__to_sort_1(self):
        nums = [42]
        expected_output = [42]
        assert comb_sort(nums) == expected_output

    def test_write_all_the__cases_for_this__to_sort_2(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        assert comb_sort(nums) == expected_output

    def test_write_all_the__cases_for_this__to_sort_3(self):
        nums = [5, 4, 3, 2, 1]
        expected_output = [1, 2, 3, 4, 5]
        assert comb_sort(nums) == expected_output

    def test_write_all_the__cases_for_this__to_sort_4(self):
        nums = [3, 3, 2, 1, 4, 4, 5, 5]
        expected_output = [1, 2, 3, 3, 4, 4, 5, 5]
        assert comb_sort(nums) == expected_output

    def test_multiple_spaces_7(self):
        nums = [0, -1, 4, -5, 3]
        expected_output = [-5, -1, 0, 3, 4]
        assert comb_sort(nums) == expected_output

    def test_write_all_the__cases_for_this__to_sort_5(self):
        nums = [3.1, 2.4, 5.6, 1.2, 4.9]
        expected_output = [1.2, 2.4, 3.1, 4.9, 5.6]
        assert comb_sort(nums) == expected_output

    def test_write_all_the__cases_for_this__to_sort_6(self):
        nums = [4.2, 2, 3.5, 1, 2.8]
        expected_output = [1, 2, 2.8, 3.5, 4.2]
        assert comb_sort(nums) == expected_output

