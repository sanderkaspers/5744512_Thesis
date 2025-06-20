import unittest
from datasets.GPT_4.Zero_shot.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        n = 15
        expected_output = True
        assert dif_Square(n) == expected_output

    def test_multiple_spaces_2(self):
        n = 6
        expected_output = False
        assert dif_Square(n) == expected_output

    def test_multiple_spaces_3(self):
        n = 0
        expected_output = True
        assert dif_Square(n) == expected_output

    def test_multiple_spaces_4(self):
        n = -5
        expected_output = True
        assert dif_Square(n) == expected_output

    def test_multiple_spaces_5(self):
        n = 1000003
        expected_output = True
        assert dif_Square(n) == expected_output

    def test_multiple_spaces_6(self):
        n = 14
        expected_output = False
        assert dif_Square(n) == expected_output

    def test_multiple_spaces_7(self):
        n = 1
        expected_output = True
        assert dif_Square(n) == expected_output

