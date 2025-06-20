import unittest
from datasets.GPT_4.Zero_shot.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        r = 5
        expected_output = 2 * 3.141592653589793 * 5  # Basic case with positive integer radius
        assert circle_circumference(r) == expected_output

    def test_multiple_spaces_2(self):
        r = 0
        expected_output = 0  # Radius is zero, so circumference should be zero
        assert circle_circumference(r) == expected_output

    def test_multiple_spaces_3(self):
        r = -3
        try:
            circle_circumference(r)
            assert False, "Expected a ValueError due to negative radius"
        except ValueError:
            pass  # Assuming the function raises a ValueError

    def test_multiple_spaces_4(self):
        r = 2.5
        expected_output = 2 * 3.141592653589793 * 2.5  # Floating-point radius
        assert circle_circumference(r) == expected_output

    def test_multiple_spaces_5(self):
        r = 1000000
        expected_output = 2 * 3.141592653589793 * 1000000  # Very large radius
        assert circle_circumference(r) == expected_output

    def test_multiple_spaces_6(self):
        r = "ten"
        try:
            circle_circumference(r)
            assert False, "Expected a TypeError due to non-numeric input"
        except TypeError:
            pass  # Assuming the function raises a TypeError


