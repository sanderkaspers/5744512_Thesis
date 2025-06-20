import unittest
from datasets.GPT_4.Zero_shot2.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_str_1(self):
        result = str_to_list("abc")
        self.assertEqual(result[ord('a')], 1)
        self.assertEqual(result[ord('b')], 1)
        self.assertEqual(result[ord('c')], 1)

    def test_str_2(self):
        result = str_to_list("aaa")
        self.assertEqual(result[ord('a')], 3)

    def test_str_3(self):
        result = str_to_list("")
        self.assertEqual(sum(result), 0)

    def test_str_4(self):
        result = str_to_list("Hello, World!")
        self.assertEqual(result[ord('H')], 1)
        self.assertEqual(result[ord(',')], 1)
        self.assertEqual(result[ord(' ')], 1)
        self.assertEqual(result[ord('!')], 1)

    def test_str_5(self):
        result = str_to_list("AaBb")
        self.assertEqual(result[ord('A')], 1)
        self.assertEqual(result[ord('a')], 1)

