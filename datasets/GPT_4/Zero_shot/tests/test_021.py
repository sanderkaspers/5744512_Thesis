import unittest
from datasets.GPT_4.Zero_shot.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this__to_chec(self):
        l = [1, 2, 3, 4, 5]
        s = [1, 2]
        expected_output = True
        assert is_sublist(l, s) == expected_output

    def test_write_all_the__cases_for_this__to_chec_1(self):
        l = [1, 2, 3, 4, 5]
        s = [4, 5]
        expected_output = True
        assert is_sublist(l, s) == expected_output

    def test_write_all_the__cases_for_this__to_chec_2(self):
        l = [1, 2, 3, 4, 5]
        s = [2, 3, 4]
        expected_output = True
        assert is_sublist(l, s) == expected_output

    def test_write_all_the__cases_for_this__to_chec_3(self):
        l = [1, 2, 3]
        s = [1, 2, 3]
        expected_output = True
        assert is_sublist(l, s) == expected_output

    def test_write_all_the__cases_for_this__to_chec_4(self):
        l = [1, 2, 3, 4, 5]
        s = [6, 7]
        expected_output = False
        assert is_sublist(l, s) == expected_output

    def test_multiple_spaces_6(self):
        l = [1, 2, 3, 4, 5]
        s = []
        expected_output = True
        assert is_sublist(l, s) == expected_output

    def test_multiple_spaces_7(self):
        l = []
        s = [1, 2]
        expected_output = False
        assert is_sublist(l, s) == expected_output

    def test_write_all_the__cases_for_this__to_chec_5(self):
        l = [1, 2]
        s = [1, 2, 3]
        expected_output = False
        assert is_sublist(l, s) == expected_output

    def test_write_all_the__cases_for_this__to_chec_6(self):
        l = [1, 2, 2, 3, 4, 2, 2, 5]
        s = [2, 2, 5]
        expected_output = True
        assert is_sublist(l, s) == expected_output

