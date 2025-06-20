import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(word_len('apple pie banana'))  # 'apple' has odd length

    def test_all_even_length(self):
        self.assertFalse(word_len('test this code'))

    def test_all_odd_length(self):
        self.assertTrue(word_len('odd len word'))

    def test_single_word_even(self):
        self.assertFalse(word_len('even'))

    def test_single_word_odd(self):
        self.assertTrue(word_len('odd'))

    def test_empty_string(self):
        self.assertFalse(word_len(''))

    def test_special_characters(self):
        self.assertTrue(word_len('hello! @home'))

    def test_string_with_numbers(self):
        self.assertTrue(word_len('123 4567'))

    def test_mixed_case_words(self):
        self.assertTrue(word_len('TestCase PassFail'))

    def test_whitespace_handling(self):
        self.assertTrue(word_len('  spaced out   words   '))  # 'out' has odd length

