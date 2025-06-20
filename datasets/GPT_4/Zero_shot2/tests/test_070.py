import unittest
from datasets.GPT_4.Zero_shot2.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_long_1(self):
        self.assertEqual(long_words(3, "This is a test string"), ["This", "test", "string"])

    def test_long_2(self):
        self.assertEqual(long_words(6, "short small big"), [])

    def test_long_3(self):
        self.assertEqual(long_words(2, "apple banana cherry"), ["apple", "banana", "cherry"])

    def test_long_4(self):
        self.assertEqual(long_words(5, ""), [])

    def test_long_5(self):
        self.assertEqual(long_words(4, "four five six seven"), ["seven"])

    def test_long_6(self):
        self.assertEqual(long_words(2, "hi  there  how  are  you"), ["there"])

    def test_long_7(self):
        self.assertEqual(long_words(3, "hello, world! wow."), ["hello,", "world!"])

    def test_long_8(self):
        self.assertEqual(long_words(0, "hi"), ["hi"])

    def test_long_9(self):
        self.assertEqual(long_words(-1, "abc def"), ["abc", "def"])

    def test_long_10(self):
        self.assertEqual(long_words(3, "Word word WORD"), ["Word", "word", "WORD"])

