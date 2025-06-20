import unittest
from datasets.GPT_4.Few_shot2.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_word_len_basic(self): self.assertEqual(word_len('hello world'), [5, 5])

    def test_word_len_with_extra_spaces(self): self.assertEqual(word_len('hello   world'), [5, 0, 0, 5])

    def test_word_len_empty_string(self): self.assertEqual(word_len(''), [0])

    def test_word_len_leading_trailing_spaces(self): self.assertEqual(word_len('  hello world  '), [0, 0, 5, 5, 0, 0])

    def test_word_len_single_word(self): self.assertEqual(word_len('python'), [6])

    def test_word_len_all_spaces(self): self.assertEqual(word_len('     '), [0, 0, 0, 0, 0, 0])

    def test_word_len_mixed_whitespace(self): self.assertEqual(word_len('a  b c'), [1, 0, 1, 1])

    def test_word_len_special_characters(self): self.assertEqual(word_len('hello@world! test#123'), [11, 8])

    def test_word_len_numbers_and_text(self): self.assertEqual(word_len('abc 123 45'), [3, 3, 2])

    def test_word_len_multiple_spaces_end(self): self.assertEqual(word_len('a b '), [1, 1, 0])

