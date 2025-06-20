import unittest
from datasets.GPT_4.Zero_shot1.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_Char("ABC"), ord('A') + ord('B') + ord('C'))

    def test_2(self):
        self.assertEqual(get_Char("123"), ord('1') + ord('2') + ord('3'))

    def test_3(self):
        self.assertEqual(get_Char("!@#"), ord('!') + ord('@') + ord('#'))

    def test_4(self):
        self.assertEqual(get_Char("aB1! "), sum(ord(c) for c in "aB1! "))

    def test_5(self):
        self.assertEqual(get_Char(""), 0)

    def test_6(self):
        self.assertEqual(get_Char("   "), ord(' ') * 3)

    def test_7(self):
        self.assertEqual(get_Char("ñ"), ord("ñ"))

    def test_8(self):
        self.assertEqual(get_Char("a" * 1000), 1000 * ord("a"))

    def test_9(self):
        self.assertEqual(get_Char("Z"), ord("Z"))

