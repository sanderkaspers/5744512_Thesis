import unittest
from datasets.GPT_4.Zero_shot.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 3
        expected_output = 9  # Sum of elements from index 1 to 3: 2 + 3 + 4 = 9
        assert sum_range_list(list1, m, n) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [10, 20, 30]
        m = 2
        n = 2
        expected_output = 30  # Single element range, only index 2
        assert sum_range_list(list1, m, n) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [5, 10, 15, 20]
        m = 0
        n = 3
        expected_output = 50  # Sum of the entire list
        assert sum_range_list(list1, m, n) == expected_output

    def test_multiple_spaces_4(self):
        list1 = [5, 10, 15]
        m = 2
        n = 1
        try:
            sum_range_list(list1, m, n)
            assert False, "Expected a ValueError due to invalid range (m > n)"
        except ValueError:
            pass  # Assuming the function raises a ValueError for invalid range

    def test_multiple_spaces_5(self):
        list1 = []
        m = 0
        n = 0
        expected_output = 0  # Empty list should return 0
        assert sum_range_list(list1, m, n) == expected_output

    def test_multiple_spaces_6(self):
        list1 = [1, 2, 3]
        m = 0
        n = 5
        try:
            sum_range_list(list1, m, n)
            assert False, "Expected an IndexError due to out of bounds index"
        except IndexError:
            pass  # Assuming the function raises an IndexError for out of bounds

    def test_multiple_spaces_7(self):
        list1 = [1, 2, 3, 4, 5]
        m = -3
        n = -1
        expected_output = 12  # Sum from index -3 to -1: 3 + 4 + 5 = 12
        assert sum_range_list(list1, m, n) == expected_output

