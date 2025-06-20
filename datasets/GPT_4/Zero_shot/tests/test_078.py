import unittest
from datasets.GPT_4.Zero_shot.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 3  # 2^1 + 2^0
        expected_output = True
        assert is_Sum_Of_Powers_Of_Two(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 4  # 2^2
        expected_output = True
        assert is_Sum_Of_Powers_Of_Two(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 6  # 2^2 + 2^1
        expected_output = True
        assert is_Sum_Of_Powers_Of_Two(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 5  # Not representable as sum of non-zero powers of 2
        expected_output = False
        assert is_Sum_Of_Powers_Of_Two(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 0  # Zero cannot be represented as sum of non-zero powers of 2
        expected_output = False
        assert is_Sum_Of_Powers_Of_Two(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 1024  # 2^10
        expected_output = True
        assert is_Sum_Of_Powers_Of_Two(n) == expected_output

    def test_multiple_spaces_7(self):
        n = -8  # Negative number, not a valid input
        try:
            is_Sum_Of_Powers_Of_Two(n)
            assert False, "Expected a ValueError due to negative input"
        except ValueError:
            pass  # Assuming the function raises a ValueError


