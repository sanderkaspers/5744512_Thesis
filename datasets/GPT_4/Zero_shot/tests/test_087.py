import unittest
from datasets.GPT_4.Zero_shot.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 5
        expected_output = 15  # Sum of 1 + 2 + 3 + 4 + 5
        assert sum_series(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 0
        expected_output = 0  # n is less than 1, so the output should be 0
        assert sum_series(n) == expected_output

    def test_multiple_spaces_3(self):
        n = -3
        expected_output = 0  # Negative input, should return 0
        assert sum_series(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 1
        expected_output = 1  # Sum of series up to 1 is just 1
        assert sum_series(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 1000
        expected_output = 500500  # Large input, sum of series 1 to 1000
        assert sum_series(n) == expected_output

