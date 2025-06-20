import unittest
from datasets.GPT_4.Zero_shot.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        test_tuple = (1, 2, 3, 4)
        expected_output = True  # All elements are of the same type (int)
        assert check_type(test_tuple) == expected_output

    def test_multiple_spaces_2(self):
        test_tuple = (1, "two", 3.0)
        expected_output = False  # Mixed data types (int, str, float)
        assert check_type(test_tuple) == expected_output

    def test_multiple_spaces_3(self):
        test_tuple = (42,)
        expected_output = True  # Single element tuple, all elements are the same type
        assert check_type(test_tuple) == expected_output

    def test_multiple_spaces_4(self):
        test_tuple = ()
        expected_output = True  # Empty tuple should return True as there are no differing types
        assert check_type(test_tuple) == expected_output

    def test_multiple_spaces_5(self):
        test_tuple = (None, None, None)
        expected_output = True  # All elements are None, which is the same type
        assert check_type(test_tuple) == expected_output

    def test_multiple_spaces_6(self):
        test_tuple = ((1, 2), (3, 4), (5, 6))
        expected_output = True  # All elements are tuples, same type
        assert check_type(test_tuple) == expected_output

    def test_multiple_spaces_7(self):
        test_tuple = ((1, 2), [3, 4], {5, 6})
        expected_output = False  # Mixed data types: tuple, list, set
        assert check_type(test_tuple) == expected_output

