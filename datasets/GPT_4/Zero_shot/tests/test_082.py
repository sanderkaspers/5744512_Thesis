import unittest
from datasets.GPT_4.Zero_shot.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [1, 2, 3]
        list2 = [1, 4, 3]
        list3 = [1, 5, 3]
        expected_output = 2  # Two pairs of the same value at the same index
        assert count_samepair(list1, list2, list3) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list3 = [7, 8, 9]
        expected_output = 0  # No matching values at the same index
        assert count_samepair(list1, list2, list3) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [1, 1, 1]
        list2 = [1, 1, 1]
        list3 = [1, 1, 1]
        expected_output = 3  # All values match across all indices
        assert count_samepair(list1, list2, list3) == expected_output

    def test_multiple_spaces_4(self):
        list1 = []
        list2 = []
        list3 = []
        expected_output = 0  # Empty lists should return 0
        assert count_samepair(list1, list2, list3) == expected_output

    def test_multiple_spaces_5(self):
        list1 = [1]
        list2 = [2]
        list3 = [3]
        expected_output = 0  # Single element lists with different values
        assert count_samepair(list1, list2, list3) == expected_output

    def test_multiple_spaces_6(self):
        list1 = [1, 2]
        list2 = [1]
        list3 = [1, 2]
        try:
            count_samepair(list1, list2, list3)
            assert False, "Expected a ValueError due to lists of different lengths"
        except ValueError:
            pass  # Assuming the function raises a ValueError

    def test_multiple_spaces_7(self):
        list1 = [i for i in range(1000)]
        list2 = [i for i in range(1000)]
        list3 = [i for i in range(1000)]
        expected_output = 1000  # Large lists where all values match
        assert count_samepair(list1, list2, list3) == expected_output

