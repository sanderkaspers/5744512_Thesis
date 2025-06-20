import unittest
from datasets.mbpp.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_next_smallest_palindrome_with_99_expect_101(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

    def test_next_smallest_palindrome_with_1221_expect_1331(self):
        self.assertEqual(next_smallest_palindrome(1221), 1331)

    def test_next_smallest_palindrome_with_120_expect_121(self):
        self.assertEqual(next_smallest_palindrome(120), 121)

