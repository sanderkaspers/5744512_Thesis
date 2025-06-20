import unittest
from datasets.GPT_4.Zero_shot.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        A = [2, 4, 6, 8]
        expected_output = 6  # There are 6 pairs of even numbers: (2,4), (2,6), (2,8), (4,6), (4,8), (6,8)
        assert find_even_pair(A) == expected_output

    def test_multiple_spaces_2(self):
        A = [1, 3, 5, 7]
        expected_output = 0  # No even numbers, so no pairs
        assert find_even_pair(A) == expected_output

    def test_multiple_spaces_3(self):
        A = [2, 2, 2, 2]
        expected_output = 6  # All even numbers, there are 6 pairs: (2,2), (2,2), (2,2)
        assert find_even_pair(A) == expected_output

    def test_multiple_spaces_4(self):
        A = [2]
        expected_output = 0  # Only one even number, no pairs can be formed
        assert find_even_pair(A) == expected_output

    def test_multiple_spaces_5(self):
        A = []
        expected_output = 0  # Empty list, no pairs can be formed
        assert find_even_pair(A) == expected_output

    def test_multiple_spaces_6(self):
        A = [2, 4, 6, 4, 2]
        expected_output = 10  # Duplicates present, counting all valid pairs
        assert find_even_pair(A) == expected_output

    def test_multiple_spaces_7(self):
        A = [1, 2, 3, 4, 5, 6]
        expected_output = 3  # Three pairs: (2,4), (2,6), (4,6)
        assert find_even_pair(A) == expected_output

