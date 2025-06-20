import unittest
from datasets.GPT_4.Zero_shot.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 3
        expected_output = 15  # 3 * (2*3 - 1) = 15
        assert hexagonal_num(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 0
        expected_output = 0  # 0 * (2*0 - 1) = 0
        assert hexagonal_num(n) == expected_output

    def test_multiple_spaces_3(self):
        n = -2
        try:
            hexagonal_num(n)
            assert False, "Expected a ValueError due to negative input"
        except ValueError:
            pass  # Assuming the function raises a ValueError

    def test_multiple_spaces_4(self):
        n = 1000
        expected_output = 1000 * (2 * 1000 - 1)  # Large input to check performance
        assert hexagonal_num(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 1
        expected_output = 1  # 1 * (2*1 - 1) = 1
        assert hexagonal_num(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 2.5
        try:
            hexagonal_num(n)
            assert False, "Expected a TypeError due to non-integer input"
        except TypeError:
            pass  # Assuming the function raises a TypeError


