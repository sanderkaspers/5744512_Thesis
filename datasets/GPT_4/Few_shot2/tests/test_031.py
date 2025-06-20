import unittest
from datasets.GPT_4.Few_shot2.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_get_Char_basic_ascii(self): self.assertEqual(get_Char('ABC'), chr((65+66+67) % 256))

    def test_get_Char_lowercase(self): self.assertEqual(get_Char('abc'), chr((97+98+99) % 256))

    def test_get_Char_numbers(self): self.assertEqual(get_Char('123'), chr((49+50+51) % 256))

    def test_get_Char_mixed_characters(self): self.assertEqual(get_Char('A1b!'), chr((65+49+98+33) % 256))

    def test_get_Char_empty_string(self): self.assertEqual(get_Char(''), chr(0))

    def test_get_Char_whitespace(self): self.assertEqual(get_Char(' '), chr(32))

    def test_get_Char_unicode_high(self): self.assertEqual(get_Char('é'), chr(ord('é') % 256))

    def test_get_Char_multiple_same_chars(self): self.assertEqual(get_Char('aaa'), chr((3 * ord('a')) % 256))

    def test_get_Char_max_ascii(self): self.assertEqual(get_Char('ÿ'), chr(255 % 256))

    def test_get_Char_wraparound(self): self.assertEqual(get_Char(chr(300)), chr(ord(chr(300)) % 256))

