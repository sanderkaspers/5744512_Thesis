import unittest
from datasets.GPT_4.Zero_shot1.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len_log(["hi", "there", "hello"]), "there")

    def test_2(self):
        self.assertEqual(len_log(["word"]), "word")

    def test_3(self):
        self.assertEqual(len_log(["aa", "bb", "cc"]), "aa")

    def test_4(self):
        self.assertEqual(len_log(["", "", "a"]), "a")

    def test_5(self):
        self.assertEqual(len_log(["", "longword", "tiny"]), "longword")

    def test_6(self):
        self.assertEqual(len_log(["longest", "mid", "short"]), "longest")

    def test_7(self):
        self.assertEqual(len_log(["tiny", "mid", "longest"]), "longest")

    def test_8(self):
        self.assertEqual(len_log(["a b", "abc", "de f"]), "abc")

    def test_9(self):
        self.assertEqual(len_log(["café", "resume", "niño"]), "resume")

    def test_10(self):
        self.assertEqual(len_log(["Hello", "HELLO", "HeLLo"]), "Hello")

    def test_11(self):
        self.assertEqual(len_log(["123", "12345", "12"]), "12345")

    def test_12(self):
        self.assertEqual(len_log([" ", "   ", ""]), "   ")

