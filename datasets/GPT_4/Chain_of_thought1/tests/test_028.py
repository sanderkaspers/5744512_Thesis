import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_standard_sentence(self): self.assertEqual(word_len('hello world'), [5, 5])

    def test_multiple_spaces(self): self.assertEqual(word_len('hi  there'), [2, 0, 5])

    def test_leading_trailing_spaces(self): self.assertEqual(word_len('  a b  '), [0, 0, 1, 1, 0])

    def test_all_spaces(self): self.assertEqual(word_len('     '), [0, 0, 0, 0, 0, 0])

    def test_single_word(self): self.assertEqual(word_len('OpenAI'), [6])

    def test_empty_string(self): self.assertEqual(word_len(''), [0])

    def test_punctuation(self): self.assertEqual(word_len('hello, world!'), [6, 6])

    def test_numbers(self): self.assertEqual(word_len('123 4567'), [3, 4])

    def test_tabs_newlines(self): self.assertEqual(word_len('line1\nline2\tline3'), [17])

