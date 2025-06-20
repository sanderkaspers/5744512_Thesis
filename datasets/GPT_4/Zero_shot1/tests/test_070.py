import unittest
from datasets.GPT_4.Zero_shot1.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(long_words(3, "this is a test"), ["this", "test"])

    def test_2(self):
        self.assertEqual(long_words(5, "cat dog bat"), [])

    def test_3(self):
        self.assertEqual(long_words(2, ""), [])

    def test_4(self):
        self.assertEqual(long_words(4, "word four shot"), [])

    def test_5(self):
        self.assertEqual(long_words(3, "well-done job!"), ["well-done", "job!"])

    def test_6(self):
        self.assertEqual(long_words(0, "a b c"), ["a", "b", "c"])

    def test_7(self):
        self.assertEqual(long_words(2, "hi   hello     world"), ["hello", "world"])

    def test_8(self):
        self.assertEqual(long_words(1, "🔥🌟 emoji"), ["emoji"])

