import unittest
from datasets.GPT_4.Zero_shot2.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_char_1(self):
        self.assertEqual(max_occurrences("aabbbcccc"), 'c')

    def test_char_2(self):
        self.assertEqual(max_occurrences("abc"), 'a')

    def test_char_3(self):
        self.assertEqual(max_occurrences("hello world!"), 'l')

    def test_char_4(self):
        self.assertEqual(max_occurrencesr("AaAaBb"), 'A')

    def test_char_5(self):
        self.assertEqual(max_occurrences("1233211"), '1')

    def test_char_6(self):
        self.assertEqual(max_occurrences("x" * 1000 + "y" * 999), 'x')

