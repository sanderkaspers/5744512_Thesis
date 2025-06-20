import unittest
from datasets.GPT_4.Zero_shot2.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_lenlog_1(self):
        self.assertEqual(len_log(["a", "ab", "abc"]), 3)

    def test_lenlog_2(self):
        self.assertEqual(len_log(["one", "two", "six"]), 3)

    def test_lenlog_3(self):
        self.assertEqual(len_log(["singleton"]), 9)

    def test_lenlog_4(self):
        self.assertEqual(len_log(["longest", "a", "b"]), 7)

    def test_lenlog_5(self):
        self.assertEqual(len_log(["a", "b", "longest"]), 7)

    def test_lenlog_6(self):
        self.assertEqual(len_log(["", "ab", "abc"]), 3)

    def test_lenlog_7(self):
        self.assertEqual(len_log(["", "", ""]), 0)

    def test_lenlog_8(self):
        self.assertEqual(len_log(["!@#", "$$$$", "%"]), 4)

    def test_lenlog_9(self):
        self.assertEqual(len_log(["123", "4567", "89"]), 4)

    def test_lenlog_10(self):
        self.assertEqual(len_log(["ABC", "abc", "AbCde"]), 5)

    def test_lenlog_11(self):
        self.assertEqual(len_log(["x" * 1000, "short"]), 1000)

    def test_lenlog_12(self):
        self.assertEqual(len_log(["éé", "ü", "你好"]), 2)

    def test_lenlog_13(self):
        self.assertEqual(len_log(["tiny", "bigger", "massiveeeeeee"]), 13)

    def test_lenlog_14(self):
        self.assertEqual(len_log(["same", "same", "same"]), 4)

