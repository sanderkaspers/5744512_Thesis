import unittest
from datasets.GPT_4.Zero_shot1.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Find_Min_Length(["hi", "hello", "hey"]), "hi")

    def test_2(self):
        self.assertEqual(Find_Min_Length(["a", "b", "cde"]), "a")

    def test_3(self):
        self.assertEqual(Find_Min_Length(["word"]), "word")

    def test_4(self):
        self.assertEqual(Find_Min_Length(["", "", ""]), "")

    def test_5(self):
        self.assertEqual(Find_Min_Length(["", "a", "abc"]), "")

    def test_6(self):
        self.assertEqual(Find_Min_Length(["longest", "mid", "s"]), "s")

    def test_7(self):
        self.assertEqual(Find_Min_Length(["a", "ab", "abc"]), "a")

    def test_8(self):
        self.assertEqual(Find_Min_Length(["café", "ño", "ü"]), "ü")

    def test_9(self):
        self.assertEqual(Find_Min_Length([" ", "  ", "    "]), " ")

    def test_10(self):
        self.assertEqual(Find_Min_Length(["aaa", "bbb", "ccc"]), "aaa")

    def test_11(self):
        self.assertEqual(Find_Min_Length(["1234", "1", "123"]), "1")

    def test_12(self):
        self.assertEqual(Find_Min_Length(["A", "b", "C"]), "A")

    def test_13(self):
        self.assertEqual(Find_Min_Length(["aa", "bb", "cc"]), "aa")

    def test_14(self):
        lst = ["long"] * 9999 + ["s"]
        self.assertEqual(Find_Min_Length(lst), "s")

