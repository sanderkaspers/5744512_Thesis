import unittest
from datasets.GPT_4.Zero_shot.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        num = 1
        expected_output = 2
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_2(self):
        num = 9
        expected_output = 11
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_3(self):
        num = 12
        expected_output = 22
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_4(self):
        num = 123
        expected_output = 131
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_5(self):
        num = 99
        expected_output = 101
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_6(self):
        num = 12321
        expected_output = 12421
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_7(self):
        num = 1000
        expected_output = 1001
        assert next_smallest_palindrome(num) == expected_output

    def test_multiple_spaces_8(self):
        num = 999999
        expected_output = 1000001
        assert next_smallest_palindrome(num) == expected_output

