import unittest
from datasets.GPT_4.Zero_shot1.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(remove_Occ("abacada", "a"), "bacad")

    def test_2(self):
        self.assertEqual(remove_Occ("aaaaaa", "a"), "aaaa")

    def test_3(self):
        self.assertEqual(remove_Occ("abc", "x"), "abc")

    def test_4(self):
        self.assertEqual(remove_Occ("xabcx", "x"), "abc")

    def test_5(self):
        self.assertEqual(remove_Occ("xabcxabcx", "x"), "abcxabc")

    def test_6(self):
        self.assertEqual(remove_Occ("mississippi", "s"), "miissippi")

    def test_7(self):
        self.assertEqual(remove_Occ("mississippi", "i"), "msssissippi")

    def test_8(self):
        self.assertEqual(remove_Occ("ababab", "b"), "aaab")

    def test_9(self):
        self.assertEqual(remove_Occ("", "a"), "")

