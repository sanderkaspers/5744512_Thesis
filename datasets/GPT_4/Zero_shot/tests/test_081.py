import unittest
from datasets.GPT_4.Zero_shot.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        nums = [3, 2, 4, 1]
        expected_output = [1, 2, 3, 4]  # Basic case with random order
        assert pancake_sort(nums) == expected_output

    def test_multiple_spaces_2(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]  # Already sorted list
        assert pancake_sort(nums) == expected_output

    def test_multiple_spaces_3(self):
        nums = [5, 4, 3, 2, 1]
        expected_output = [1, 2, 3, 4, 5]  # Reversed list
        assert pancake_sort(nums) == expected_output

    def test_multiple_spaces_4(self):
        nums = [3, 3, 2, 1, 2]
        expected_output = [1, 2, 2, 3, 3]  # List with duplicates
        assert pancake_sort(nums) == expected_output

    def test_multiple_spaces_5(self):
        nums = [42]
        expected_output = [42]  # Single element list
        assert pancake_sort(nums) == expected_output

    def test_multiple_spaces_6(self):
        nums = []
        expected_output = []  # Empty list should return an empty list
        assert pancake_sort(nums) == expected_output

    def test_multiple_spaces_7(self):
        nums = [i for i in range(1000, 0, -1)]
        expected_output = [i for i in range(1, 1001)]  # Large reversed list
        assert pancake_sort(nums) == expected_output

