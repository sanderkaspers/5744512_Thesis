import unittest
from datasets.GPT_4.Few_shot.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(next_smallest_palindrome(123), 131) # Small number)

    def test_case_2(self):
        self.assertEqual(next_smallest_palindrome(9), 11) # Single-digit number)

    def test_case_3(self):
        self.assertEqual(next_smallest_palindrome(121), 131) # Already a palindrome)

    def test_case_4(self):
        self.assertEqual(next_smallest_palindrome(808), 818) # Palindromic number)

    def test_case_5(self):
        self.assertEqual(next_smallest_palindrome(999), 1001) # Largest 3-digit number)

    def test_case_6(self):
        self.assertEqual(next_smallest_palindrome(1), 2) # Smallest number)

    def test_case_7(self):
        self.assertEqual(next_smallest_palindrome(12321), 12421) # Large palindrome)

    def test_case_8(self):
        self.assertEqual(next_smallest_palindrome(100), 101) # Round number)

