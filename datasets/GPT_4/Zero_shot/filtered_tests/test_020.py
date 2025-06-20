import unittest
from datasets.GPT_4.Zero_shot.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this(self):
        A = [1, 2, 3, 4, 5]
        expected_output = True
        assert is_Monotonic(A) == expected_output

    def test_write_all_the__cases_for_this_1(self):
        A = [5, 4, 3, 2, 1]
        expected_output = True
        assert is_Monotonic(A) == expected_output

    def test_multiple_spaces_3(self):
        A = []
        expected_output = True
        assert is_Monotonic(A) == expected_output

    def test_write_all_the__cases_for_this_2(self):
        A = [7]
        expected_output = True
        assert is_Monotonic(A) == expected_output

    def test_write_all_the__cases_for_this_3(self):
        A = [4, 4, 4, 4]
        expected_output = True
        assert is_Monotonic(A) == expected_output

    def test_write_all_the__cases_for_this_4(self):
        A = [1, 3, 2, 4, 5]
        expected_output = False
        assert is_Monotonic(A) == expected_output

    def test_write_all_the__cases_for_this_5(self):
        A = [1, 2, 3, 2, 1]
        expected_output = False
        assert is_Monotonic(A) == expected_output

    def test_multiple_spaces_8(self):
        A = [1000, 2000, 3000, 3000, 4000]
        expected_output = True
        assert is_Monotonic(A) == expected_output

    def test_multiple_spaces_9(self):
        A = [4000, 3000, 3000, 2000, 1000]
        expected_output = True
        assert is_Monotonic(A) == expected_output

