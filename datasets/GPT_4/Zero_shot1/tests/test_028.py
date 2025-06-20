import unittest
from datasets.GPT_4.Zero_shot1.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(word_len("hello, world!"), [6, 6])

    def test_2(self):
        self.assertEqual(word_len("a  b   c"), [1, 0, 1, 0, 1])

    def test_3(self):
        self.assertEqual(word_len(""), [0])

    def test_4(self):
        self.assertEqual(word_len("     "), [0, 0, 0, 0, 0, 0])

    def test_5(self):
        self.assertEqual(word_len("Python"), [6])

    def test_6(self):
        self.assertEqual(word_len("test "), [4, 0])

    def test_7(self):
        self.assertEqual(word_len(" test"), [0, 4])

    def test_8(self):
        self.assertEqual(word_len("a\tb"), [3])

    def test_9(self):
        self.assertEqual(word_len("supercalifragilisticexpialidocious"), [34])

    def test_10(self):
        self.assertEqual(word_len("a b c"), [1, 1, 1])

    def test_11(self):
        self.assertEqual(word_len("Test CASE"), [4, 4])

    def test_12(self):
        self.assertEqual(word_len("naïve façade"), [5, 6])

    def test_13(self):
        self.assertEqual(word_len("line1\nline2"), [11])

    def test_14(self):
        self.assertEqual(word_len("123 4567"), [3, 4])

