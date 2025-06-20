import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_normal_tuple(self): self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_single_element(self): self.assertEqual(tup_string(('x',)), 'x')

    def test_empty_tuple(self): self.assertEqual(tup_string(()), '')

    def test_space_in_tuple(self): self.assertEqual(tup_string(('h', 'e', ' ', 'l', 'l', 'o')), 'he llo')

    def test_digit_strings(self): self.assertEqual(tup_string(('1', '2', '3')), '123')

    def test_special_chars(self): self.assertEqual(tup_string(('@', '#', '$')), '@#$')

    def test_unicode(self): self.assertEqual(tup_string(('你', '好')), '你好')

    def test_newlines_tabs(self): self.assertEqual(tup_string(('a', '\n', 'b', '\t')), 'a\nb\t')

    def test_multi_char_strings(self): self.assertEqual(tup_string(('abc', 'def')), 'abcdef')

