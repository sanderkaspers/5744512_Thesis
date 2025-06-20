import unittest
from datasets.GPT_4.Zero_shot2.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_pal_1(self):
        self.assertEqual(next_smallest_palindrome(123), 131)

    def test_pal_2(self):
        self.assertEqual(next_smallest_palindrome(131), 141)

    def test_pal_3(self):
        self.assertEqual(next_smallest_palindrome(999), 1001)

    def test_pal_4(self):
        self.assertEqual(next_smallest_palindrome(808), 818)

    def test_pal_5(self):
        self.assertEqual(next_smallest_palindrome(5), 6)

    def test_pal_6(self):
        self.assertEqual(next_smallest_palindrome(123456789), 123464321)

