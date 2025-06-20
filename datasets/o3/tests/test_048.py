import unittest
from datasets.o3.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(next_smallest_palindrome(9), 11)

    def test_palindrome_input(self):
        self.assertEqual(next_smallest_palindrome(11), 22)

    def test_three_digit(self):
        self.assertEqual(next_smallest_palindrome(123), 131)

    def test_cross_century(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

    def test_palindrome_large(self):
        self.assertEqual(next_smallest_palindrome(12321), 12421)

    def test_mixed_digits(self):
        self.assertEqual(next_smallest_palindrome(191), 202)

