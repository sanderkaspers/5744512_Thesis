import unittest
from datasets.GPT_4.Zero_shot1.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertTrue(find_substring("hello", "e"))

    def test_2(self):
        self.assertTrue(find_substring("hello", "leo"))

    def test_3(self):
        self.assertFalse(find_substring("hello", "xyz"))

    def test_4(self):
        self.assertFalse(find_substring("hello", ""))

    def test_5(self):
        self.assertFalse(find_substring("", "hello"))

    def test_6(self):
        self.assertFalse(find_substring("", ""))

    def test_7(self):
        self.assertFalse(find_substring("HELLO", "hello"))

    def test_8(self):
        self.assertTrue(find_substring("12345", "6789"))

    def test_9(self):
        self.assertTrue(find_substring("!@#", "@!"))

    def test_10(self):
        self.assertTrue(find_substring("hi", "hiiiiiiiiiiiiiiiiiiiiiiii"))

    def test_11(self):
        self.assertTrue(find_substring("café", "é"))

    def test_12(self):
        self.assertTrue(find_substring("hi there", " "))

    def test_13(self):
        self.assertTrue(find_substring("end", "d"))

    def test_14(self):
        self.assertTrue(find_substring("start", "s"))

    def test_15(self):
        self.assertTrue(find_substring("aaa", "aa"))

    def test_16(self):
        self.assertFalse(find_substring("abc", "x" * 10000))

    def test_17(self):
        self.assertTrue(find_substring("abc", "x" * 9999 + "a"))

    def test_18(self):
        self.assertTrue(find_substring("same", "same"))

