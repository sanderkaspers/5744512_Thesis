import unittest
from datasets.GPT_4.Zero_shot.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        nums = [1, -2, 3, -4, 5]
        expected_output = -6  # Sum of -2 and -4
        assert sum_negativenum(nums) == expected_output

    def test_multiple_spaces_2(self):
        nums = [-1, -2, -3]
        expected_output = -6  # Sum of all negative numbers
        assert sum_negativenum(nums) == expected_output

    def test_multiple_spaces_3(self):
        nums = [1, 2, 3, 4]
        expected_output = 0  # No negative numbers
        assert sum_negativenum(nums) == expected_output

    def test_multiple_spaces_4(self):
        nums = [0, -1, 0, -2, 0]
        expected_output = -3  # Sum of -1 and -2
        assert sum_negativenum(nums) == expected_output

    def test_multiple_spaces_5(self):
        nums = []
        expected_output = 0  # Empty list should return 0
        assert sum_negativenum(nums) == expected_output

    def test_multiple_spaces_6(self):
        nums = [-10]
        expected_output = -10  # Single negative number
        assert sum_negativenum(nums) == expected_output

    def test_multiple_spaces_7(self):
        nums = [0, 0, 0]
        expected_output = 0  # No negative numbers, only zeros
        assert sum_negativenum(nums) == expected_output

