import unittest
from datasets.GPT_4.Zero_shot.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        arr = [1, 3, 7, 2]
        expected_output = 7321
        assert find_Max_Num(arr) == expected_output

    def test_multiple_spaces_2(self):
        arr = [5, 5, 3]
        expected_output = 553
        assert find_Max_Num(arr) == expected_output

    def test_write_all_the__cases_for_this(self):
        arr = [9]
        expected_output = 9
        assert find_Max_Num(arr) == expected_output

    def test_multiple_spaces_4(self):
        arr = [0, 0, 1]
        expected_output = 100
        assert find_Max_Num(arr) == expected_output

    def test_multiple_spaces_5(self):
        arr = [1, 2, 3, 4]
        expected_output = 4321
        assert find_Max_Num(arr) == expected_output

    def test_multiple_spaces_6(self):
        arr = [9, 8, 7, 6]
        expected_output = 9876
        assert find_Max_Num(arr) == expected_output

    def test_multiple_spaces_7(self):
        arr = []
        expected_output = 0
        assert find_Max_Num(arr) == expected_output

