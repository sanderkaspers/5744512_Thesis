import unittest
from datasets.GPT_4.Zero_shot.programs.program_066 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        a = 1 + 1j
        b = 1 + 2j
        expected_output = cmath.phase((1 + 2j) / (1 + 1j))
        assert angle_complex(a, b) == expected_output

    def test_multiple_spaces_2(self):
        a = 2 + 3j
        b = 2 + 3j
        expected_output = 0  # Identical complex numbers
        assert angle_complex(a, b) == expected_output

    def test_multiple_spaces_3(self):
        a = 1 + 2j
        b = 1 - 2j
        expected_output = cmath.phase((1 - 2j) / (1 + 2j))
        assert angle_complex(a, b) == expected_output

    def test_multiple_spaces_4(self):
        a = 3 + 0j
        b = 4 + 0j
        expected_output = cmath.phase((4 + 0j) / (3 + 0j))  # Both purely real numbers
        assert angle_complex(a, b) == expected_output

    def test_multiple_spaces_5(self):
        a = 0 + 3j
        b = 0 + 4j
        expected_output = cmath.phase((0 + 4j) / (0 + 3j))  # Both purely imaginary numbers
        assert angle_complex(a, b) == expected_output

    def test_multiple_spaces_6(self):
        a = -1 - 1j
        b = -1 - 2j
        expected_output = cmath.phase((-1 - 2j) / (-1 - 1j))
        assert angle_complex(a, b) == expected_output

    def test_multiple_spaces_7(self):
        a = 0 + 0j
        b = 1 + 1j
        try:
            angle_complex(a, b)
            assert False, "Expected a ValueError due to zero input"
        except ValueError:
            pass  # Assuming the function raises a ValueError


