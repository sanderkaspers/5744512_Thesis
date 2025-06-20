import unittest
from datasets.GPT_4.Few_shot1.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_palindrome_next_from_1(self): self.assertEqual(next_smallest_palindrome(1), 2)

    def test_palindrome_next_from_8(self): self.assertEqual(next_smallest_palindrome(8), 9)

    def test_palindrome_next_from_9(self): self.assertEqual(next_smallest_palindrome(9), 11)

    def test_palindrome_next_from_99(self): self.assertEqual(next_smallest_palindrome(99), 101)

    def test_palindrome_next_from_123(self): self.assertEqual(next_smallest_palindrome(123), 131)

    def test_palindrome_next_from_palindrome(self): self.assertEqual(next_smallest_palindrome(121), 131)

