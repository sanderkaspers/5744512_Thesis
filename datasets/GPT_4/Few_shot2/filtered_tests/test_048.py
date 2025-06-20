import unittest
from datasets.GPT_4.Few_shot2.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_next_smallest_palindrome_after_non_palindrome(self): self.assertEqual(next_smallest_palindrome(123), 131)

    def test_next_smallest_palindrome_after_palindrome(self): self.assertEqual(next_smallest_palindrome(121), 131)

    def test_next_smallest_palindrome_single_digit(self): self.assertEqual(next_smallest_palindrome(7), 8)

    def test_next_smallest_palindrome_to_next_tens(self): self.assertEqual(next_smallest_palindrome(89), 99)

    def test_next_smallest_palindrome_to_next_hundred(self): self.assertEqual(next_smallest_palindrome(99), 101)

    def test_next_smallest_palindrome_large_number(self): self.assertEqual(next_smallest_palindrome(12321), 12421)

    def test_next_smallest_palindrome_all_nines(self): self.assertEqual(next_smallest_palindrome(999), 1001)

    def test_next_smallest_palindrome_zero(self): self.assertEqual(next_smallest_palindrome(0), 1)

    def test_next_smallest_palindrome_with_leading_zero(self): self.assertEqual(next_smallest_palindrome(9), 11)

