import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_all_lowercase_match(self): self.assertEqual(count_char_position('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_all_uppercase_match(self): self.assertEqual(count_char_position('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_mixed_case_match(self): self.assertEqual(count_char_position('aBcDeFg'), 7)

    def test_no_match(self): self.assertEqual(count_char_position('ZXYWVUT'), 0)

    def test_single_char_match(self): self.assertEqual(count_char_position('a'), 1)

    def test_single_char_no_match(self): self.assertEqual(count_char_position('b'), 0)

    def test_symbols(self): self.assertEqual(count_char_position('a#c$d'), 3)

    def test_empty_string(self): self.assertEqual(count_char_position(''), 0)

    def test_digits_and_punctuation(self): self.assertEqual(count_char_position('12345!@#$%'), 0)

    def test_unicode_input(self): self.assertEqual(count_char_position('āēīōū'), 0)

