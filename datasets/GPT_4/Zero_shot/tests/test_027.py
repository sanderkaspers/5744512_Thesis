import unittest
from datasets.GPT_4.Zero_shot.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 22
        expected_output = True
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 23
        expected_output = False
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 0
        expected_output = True
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_4(self):
        n = -33
        expected_output = True
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_5(self):
        n = -34
        expected_output = False
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 110000
        expected_output = True
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 3
        expected_output = False
        assert is_Diff(n) == expected_output

    def test_multiple_spaces_8(self):
        n = 123456789
        expected_output = False
        assert is_Diff(n) == expected_output

