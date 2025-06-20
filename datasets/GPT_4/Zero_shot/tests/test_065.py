import unittest
from datasets.GPT_4.Zero_shot.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        limit = 300
        expected_output = 504  # The sum of the amicable numbers 220 and 284
        assert amicable_numbers_sum(limit) == expected_output

    def test_multiple_spaces_2(self):
        limit = 200
        expected_output = 0  # No amicable numbers below 200
        assert amicable_numbers_sum(limit) == expected_output

    def test_multiple_spaces_3(self):
        limit = 284
        expected_output = 220  # Only 220 is counted because 284 is the limit
        assert amicable_numbers_sum(limit) == expected_output

    def test_multiple_spaces_4(self):
        limit = 10000
        expected_output = 31626  # Known sum of amicable numbers below 10000
        assert amicable_numbers_sum(limit) == expected_output

    def test_multiple_spaces_5(self):
        limit = "1000"
        try:
            amicable_numbers_sum(limit)
            assert False, "Expected a TypeError due to non-integer limit"
        except TypeError:
            pass  # Assuming the function raises a TypeError

    def test_multiple_spaces_6(self):
        limit = -1000
        expected_output = 0  # Negative limit should return 0, assuming no negative amicable numbers
        assert amicable_numbers_sum(limit) == expected_output

