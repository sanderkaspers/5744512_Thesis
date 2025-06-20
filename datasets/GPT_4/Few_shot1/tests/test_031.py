import unittest
from datasets.GPT_4.Few_shot1.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_get_char_basic(self): self.assertEqual(get_Char("abc"), ord('a') + ord('b') + ord('c'))

    def test_get_char_empty(self): self.assertEqual(get_Char(""), 0)

    def test_get_char_single_char(self): self.assertEqual(get_Char("A"), ord('A'))

    def test_get_char_numeric_string(self): self.assertEqual(get_Char("123"), ord('1') + ord('2') + ord('3'))

    def test_get_char_special_chars(self): self.assertEqual(get_Char("!@#"), ord('!') + ord('@') + ord('#'))

    def test_get_char_mixed_case(self): self.assertEqual(get_Char("aBcD"), ord('a') + ord('B') + ord('c') + ord('D'))

    def test_get_char_whitespace(self): self.assertEqual(get_Char(" \t\n"), ord(' ') + ord('\t') + ord('\n'))

    def test_get_char_long_input(self): s = "abc" * 100; self.assertEqual(get_Char(s), sum(ord(c) for c in s))

    def test_get_char_unicode(self): self.assertEqual(get_Char("ñáé"), ord('ñ') + ord('á') + ord('é'))

    def test_get_char_extended_ascii(self): self.assertEqual(get_Char(chr(255) + chr(128)), 255 + 128)

