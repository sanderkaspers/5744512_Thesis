import unittest
from datasets.GPT_4.Zero_shot1.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_char_position("ZYXWVUTSRQPONMLKJIHGFEDCBA"), 0)

    def test_2(self):
        self.assertEqual(count_char_position("aBCdefghijklmnopqrstuvwxyZ"), 1)

    def test_3(self):
        self.assertEqual(count_char_position("Z"*26), 0)

    def test_4(self):
        self.assertEqual(count_char_position(""), 0)

    def test_5(self):
        self.assertEqual(count_char_position("123!@#"), 0)

    def test_6(self):
        self.assertEqual(count_char_position("a"), 1)

    def test_7(self):
        self.assertEqual(count_char_position("b"), 0)

    def test_8(self):
        self.assertEqual(count_char_position("aAaAaAaA"), 4)

    def test_9(self):
        self.assertIsInstance(count_char_position("AbC"), int)

