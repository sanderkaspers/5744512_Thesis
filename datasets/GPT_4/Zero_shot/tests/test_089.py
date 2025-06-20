import unittest
from datasets.GPT_4.Zero_shot.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 6
        expected_output = 12  # Divisors are 1, 2, 3, 6
        assert div_sum(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 13
        expected_output = 14  # Prime number, divisors are 1 and 13
        assert div_sum(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 16
        expected_output = 31  # Perfect square, divisors are 1, 2, 4, 8, 16
        assert div_sum(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 1
        expected_output = 1  # Only divisor is 1
        assert div_sum(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 10000
        expected_output = 24843  # Large input, sum of divisors of 10000
        assert div_sum(n) == expected_output

    def test_multiple_spaces_6(self):
        n = -6
        try:
            div_sum(n)
            assert False, "Expected a ValueError due to negative input"
        except ValueError:
            pass  # Assuming the function raises a ValueError for negative input

    def test_multiple_spaces_7(self):
        n = 6.5
        try:
            div_sum(n)
            assert False, "Expected a TypeError due to non-integer input"
        except TypeError:
            pass  # Assuming the function raises a TypeError for non-integer input


