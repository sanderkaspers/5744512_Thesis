import unittest
from datasets.GPT_4.Zero_shot2.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_substring_1(self):
        self.assertEqual(count_Substrings("hello world", "world"), 1)

    def test_substring_2(self):
        self.assertEqual(count_Substrings("ababab", "ab"), 3)

    def test_substring_3(self):
        self.assertEqual(count_Substrings("aaaa", "aa"), 3)

    def test_substring_4(self):
        self.assertEqual(count_Substrings("abcdef", "gh"), 0)

    def test_substring_5(self):
        self.assertEqual(count_Substrings("abc", ""), 4)

    def test_substring_6(self):
        self.assertEqual(count_Substrings("", "a"), 0)

    def test_substring_7(self):
        self.assertEqual(count_Substrings("hi", "hello"), 0)

    def test_substring_8(self):
        self.assertEqual(count_Substrings("match", "match"), 1)

