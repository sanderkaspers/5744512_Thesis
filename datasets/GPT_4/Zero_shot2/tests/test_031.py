import unittest
from datasets.GPT_4.Zero_shot2.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_char_1(self):
        self.assertEqual(get_Char("A"), chr(ord("A") % 256))

    def test_char_2(self):
        self.assertEqual(get_Char("AB"), chr((ord("A") + ord("B")) % 256))

    def test_char_3(self):
        self.assertEqual(get_Char("abc"), chr(sum(map(ord, "abc")) % 256))

    def test_char_4(self):
        self.assertEqual(get_Char("aaa"), chr(3 * ord("a") % 256))

    def test_char_5(self):
        self.assertEqual(get_Char(""), chr(0))

    def test_char_6(self):
        self.assertEqual(get_Char("A" * 300), chr((300 * ord("A")) % 256))

    def test_char_7(self):
        self.assertTrue(0 <= ord(get_Char("€")) < 256)

