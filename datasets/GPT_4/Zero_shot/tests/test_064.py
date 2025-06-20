import unittest
from datasets.GPT_4.Zero_shot.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [(1, 2), (3, 4), (2, 5)]
        expected_output = (3, 4)  # Product of 3*4=12 is the maximum
        assert max_product_tuple(list1) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [(-1, 2), (-3, -4), (2, 5)]
        expected_output = (-3, -4)  # Product of -3*-4=12 is the maximum
        assert max_product_tuple(list1) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [(-1, 2), (3, -4), (-2, -5)]
        expected_output = (-2, -5)  # Product of -2*-5=10 is the maximum
        assert max_product_tuple(list1) == expected_output

    def test_multiple_spaces_4(self):
        list1 = [(0, 2), (3, 4), (2, 0)]
        expected_output = (3, 4)  # Product of 3*4=12 is the maximum
        assert max_product_tuple(list1) == expected_output

    def test_multiple_spaces_5(self):
        list1 = [(1, 2)]
        expected_output = (1, 2)  # Only one tuple in the list
        assert max_product_tuple(list1) == expected_output

    def test_multiple_spaces_6(self):
        list1 = []
        try:
            max_product_tuple(list1)
            assert False, "Expected an error due to empty list"
        except ValueError:
            pass  # Assuming the function raises an error

    def test_multiple_spaces_7(self):
        list1 = [(1, 2, 3), (4, 5)]
        try:
            max_product_tuple(list1)
            assert False, "Expected an error due to tuples of different lengths"
        except ValueError:
            pass  # Assuming the function raises an error


