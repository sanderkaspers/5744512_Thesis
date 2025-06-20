import unittest
from datasets.GPT_4.Zero_shot.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 121212
        expected_output = True
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 123456
        expected_output = False
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 12
        expected_output = False
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 1010101010
        expected_output = True
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 111111
        expected_output = False
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 212121
        expected_output = True
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 121214
        expected_output = False
        assert is_undulating(n) == expected_output

    def test_multiple_spaces_8(self):
        n = 1234567890
        expected_output = False
        assert is_undulating(n) == expected_output

