import unittest
from datasets.GPT_4.Zero_shot.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        nums = [0, 1, 0, 2, 3]
        expected_output = 2/3  # 2 zeros, 3 non-zeros
        assert zero_count(nums) == expected_output

    def test_multiple_spaces_2(self):
        nums = [0, 0, 0]
        try:
            zero_count(nums)
            assert False, "Expected a ZeroDivisionError due to all elements being zero"
        except ZeroDivisionError:
            pass  # Expected outcome

    def test_multiple_spaces_3(self):
        nums = [1, 2, 3]
        expected_output = 0  # No zeros, so the ratio is 0
        assert zero_count(nums) == expected_output

    def test_multiple_spaces_4(self):
        nums = [0]
        try:
            zero_count(nums)
            assert False, "Expected a ZeroDivisionError due to single zero"
        except ZeroDivisionError:
            pass  # Expected outcome

    def test_multiple_spaces_5(self):
        nums = []
        try:
            zero_count(nums)
            assert False, "Expected a ZeroDivisionError due to empty array"
        except ZeroDivisionError:
            pass  # Expected outcome

    def test_multiple_spaces_6(self):
        nums = [-1, 0, -2, 0]
        expected_output = 2/2  # 2 zeros, 2 non-zeros
        assert zero_count(nums) == expected_output

    def test_multiple_spaces_7(self):
        nums = [0] * 1000 + [1] * 1000
        expected_output = 1000/1000  # 1000 zeros, 1000 non-zeros
        assert zero_count(nums) == expected_output

