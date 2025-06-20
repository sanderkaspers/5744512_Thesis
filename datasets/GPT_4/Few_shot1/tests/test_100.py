import unittest
from datasets.GPT_4.Few_shot1.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_odd_values_string_simple(self): self.assertEqual(odd_values_string("abcdef"), "ace")

    def test_odd_values_string_single_char(self): self.assertEqual(odd_values_string("x"), "x")

    def test_odd_values_string_two_chars(self): self.assertEqual(odd_values_string("xy"), "x")

    def test_odd_values_string_empty(self): self.assertEqual(odd_values_string(""), "")

    def test_odd_values_string_spaces(self): self.assertEqual(odd_values_string("a b c d e"), "abcde")

    def test_odd_values_string_symbols(self): self.assertEqual(odd_values_string("@#$%^&*"), "@$^*")

    def test_odd_values_string_numeric(self): self.assertEqual(odd_values_string("1234567890"), "13579")

    def test_odd_values_string_mixed_case(self): self.assertEqual(odd_values_string("AbCdEfG"), "ACEG")

    def test_odd_values_string_whitespace(self): self.assertEqual(odd_values_string(" a b c "), "abc")

    def test_odd_values_string_palindrome(self): self.assertEqual(odd_values_string("racecar"), "rcea")

    def test_odd_values_string_repeating(self): self.assertEqual(odd_values_string("aaaaaa"), "aaa")

    def test_odd_values_string_long(self): self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "acegikmoqsuwy")

    def test_odd_values_string_unicode(self): self.assertEqual(odd_values_string("åß∂ƒ©˙∆˚¬"), "å∂©∆¬")

    def test_odd_values_string_emoji(self): self.assertEqual(odd_values_string("🙂🙃🙂🙃🙂🙃"), "🙂🙂🙂")

    def test_odd_values_string_newlines(self): self.assertEqual(odd_values_string("a\nb\nc\nd"), "abc")

    def test_odd_values_string_tabs(self): self.assertEqual(odd_values_string("a\tb\tc\td"), "abc")

