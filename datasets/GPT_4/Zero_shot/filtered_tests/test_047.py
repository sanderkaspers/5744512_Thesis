import unittest
from datasets.GPT_4.Zero_shot.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 0
        expected_output = "0"
        assert decimal_to_binary(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 1
        expected_output = "1"
        assert decimal_to_binary(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 2
        expected_output = "10"
        assert decimal_to_binary(n) == expected_output

    def test_multiple_spaces_4(self):
        n = 5
        expected_output = "101"
        assert decimal_to_binary(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 16
        expected_output = "10000"
        assert decimal_to_binary(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 1023
        expected_output = "1111111111"
        assert decimal_to_binary(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 19
        expected_output = "10011"
        assert decimal_to_binary(n) == expected_output

