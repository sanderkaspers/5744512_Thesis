import unittest
from datasets.GPT_4.Few_shot1.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_word_len_normal_sentence(self): self.assertEqual(word_len("hello world"), [5, 5])

    def test_word_len_single_word(self): self.assertEqual(word_len("python"), [6])

    def test_word_len_empty_string(self): self.assertEqual(word_len(""), [0])

    def test_word_len_multiple_spaces(self): self.assertEqual(word_len("hello   world"), [5, 0, 0, 5])

    def test_word_len_leading_trailing_spaces(self): self.assertEqual(word_len("  hello world  "), [0, 5, 5, 0])

    def test_word_len_only_spaces(self): self.assertEqual(word_len("     "), [0, 0, 0, 0, 0, 0])

    def test_word_len_special_characters(self): self.assertEqual(word_len("hello! world?"), [6, 6])

    def test_word_len_numbers(self): self.assertEqual(word_len("123 4567 89"), [3, 4, 2])

    def test_word_len_mixed_case(self): self.assertEqual(word_len("Hello World"), [5, 5])

    def test_word_len_unicode(self): self.assertEqual(word_len("café naïve"), [4, 5])

