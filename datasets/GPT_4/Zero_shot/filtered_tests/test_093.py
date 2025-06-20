import unittest
from datasets.GPT_4.Zero_shot.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        a = [1, 2, 3, 2, 2, 4, 2]
        x = 2
        expected_output = 4  # The element 2 appears 4 times
        assert frequency(a, x) == expected_output

    def test_multiple_spaces_2(self):
        a = [1, 2, 3, 4, 5]
        x = 6
        expected_output = 0  # The element 6 is not present in the list
        assert frequency(a, x) == expected_output

    def test_multiple_spaces_3(self):
        a = [3]
        x = 3
        expected_output = 1  # Single element list with x present
        assert frequency(a, x) == expected_output

    def test_multiple_spaces_4(self):
        a = []
        x = 3
        expected_output = 0  # Empty list should return 0
        assert frequency(a, x) == expected_output

    def test_multiple_spaces_5(self):
        a = [1, "a", 2, "b", 3, "a"]
        x = "a"
        expected_output = 2  # Mixed data types, "a" appears twice
        assert frequency(a, x) == expected_output

    def test_multiple_spaces_6(self):
        a = [2, 2, 2, 2]
        x = 2
        expected_output = 4  # All elements in the list are x
        assert frequency(a, x) == expected_output

    def test_multiple_spaces_7(self):
        a = [1] * 10000 + [2] * 5000
        x = 1
        expected_output = 10000  # Large list, x appears 10000 times
        assert frequency(a, x) == expected_output

