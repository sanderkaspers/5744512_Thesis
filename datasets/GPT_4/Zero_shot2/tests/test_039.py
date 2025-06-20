import unittest
from datasets.GPT_4.Zero_shot2.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_sub_1(self):
        self.assertTrue(find_substring("hello world", "ell"))

    def test_sub_2(self):
        self.assertTrue(find_substring("hello world", "world"))

    def test_sub_3(self):
        self.assertFalse(find_substring("hello world", "mars"))

    def test_sub_4(self):
        self.assertFalse(find_substring("hello world", "o w"))

    def test_sub_5(self):
        self.assertTrue(find_substring("hello world", ""))

    def test_sub_6(self):
        self.assertFalse(find_substring("", "any"))

    def test_sub_7(self):
        self.assertTrue(find_substring("", ""))

    def test_sub_8(self):
        self.assertTrue(find_substring("abc def", "ab"))

    def test_sub_9(self):
        self.assertTrue(find_substring("abc def", "ef"))

    def test_sub_10(self):
        self.assertFalse(find_substring("Hello World", "world"))

    def test_sub_11(self):
        self.assertTrue(find_substring("a!b c#d", "!b"))

    def test_sub_12(self):
        self.assertTrue(find_substring(" ".join(["x"] * 1000), "x"))

    def test_sub_13(self):
        self.assertTrue(find_substring("word.", "word."))

    def test_sub_14(self):
        self.assertFalse(find_substring("hello world", " "))

