import unittest
from datasets.GPT_4.Zero_shot.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        a = 5
        expected_output = 25  # Perimeter of pentagon with side length 5: 5 * 5
        assert perimeter_pentagon(a) == expected_output

    def test_multiple_spaces_2(self):
        a = 7.5
        expected_output = 37.5  # Floating-point side length: 5 * 7.5
        assert perimeter_pentagon(a) == expected_output

    def test_multiple_spaces_3(self):
        a = 0
        expected_output = 0  # Zero side length should result in a perimeter of 0
        assert perimeter_pentagon(a) == expected_output

    def test_multiple_spaces_4(self):
        a = -4
        try:
            perimeter_pentagon(a)
            assert False, "Expected a ValueError due to negative side length"
        except ValueError:
            pass  # Assuming the function raises a ValueError for negative side length

    def test_multiple_spaces_5(self):
        a = 10000
        expected_output = 50000  # Large side length: 5 * 10000
        assert perimeter_pentagon(a) == expected_output

    def test_multiple_spaces_6(self):
        a = "side"
        try:
            perimeter_pentagon(a)
            assert False, "Expected a TypeError due to non-numeric input"
        except TypeError:
            pass  # Assuming the function raises a TypeError for non-numeric input


