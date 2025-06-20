import unittest
from datasets.GPT_4.Zero_shot2.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_len_1(self):
        self.assertEqual(word_len("hello world"), [5, 5])

    def test_len_2(self):
        self.assertEqual(word_len("hi  there"), [2, 0, 5])

    def test_len_3(self):
        self.assertEqual(word_len("  hello world  "), [0, 0, 5, 5, 0])

    def test_len_4(self):
        self.assertEqual(word_len("OpenAI"), [6])

    def test_len_5(self):
        self.assertEqual(word_len(""), [0])

    def test_len_6(self):
        self.assertEqual(word_len("     "), [0, 0, 0, 0, 0, 0])

    def test_len_7(self):
        self.assertEqual(word_len("line1\nline2"), [11])

    def test_len_8(self):
        self.assertEqual(word_len("hi! how's it going?"), [3, 6, 2, 6])

