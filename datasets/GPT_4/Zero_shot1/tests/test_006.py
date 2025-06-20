import unittest
from datasets.GPT_4.Zero_shot1.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(str_to_list("testcase"), ["e", "s", "t"])

    def test_2(self):
        self.assertEqual(str_to_list("abcd"), [])

    def test_3(self):
        self.assertEqual(str_to_list("aabbcc"), ["a", "b", "c"])

    def test_4(self):
        self.assertEqual(str_to_list("AaBbCc"), [])

    def test_5(self):
        self.assertEqual(str_to_list("112233"), ["1", "2", "3"])

    def test_6(self):
        self.assertEqual(str_to_list("!!??!!"), ["!"])

    def test_7(self):
        self.assertEqual(str_to_list("Mississippi"), ["i", "p", "s"])

    def test_8(self):
        self.assertEqual(str_to_list(""), [])

    def test_9(self):
        self.assertEqual(str_to_list("abcabcABCABC"), ["A", "B", "C", "a", "b", "c"])

