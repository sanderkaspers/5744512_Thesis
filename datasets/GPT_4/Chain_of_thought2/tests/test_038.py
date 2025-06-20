import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_different_lengths(self): self.assertEqual(len_log(['cat', 'elephant', 'tiger']), 8)

    def test_same_length_words(self): self.assertEqual(len_log(['dog', 'cat', 'bat']), 3)

    def test_single_word(self): self.assertEqual(len_log(['hippopotamus']), 12)

    def test_word_with_symbols(self): self.assertEqual(len_log(['hello!', '@@@@', 'hi']), 6)

    def test_list_with_empty_string(self): self.assertEqual(len_log(['', 'a', 'ab']), 2)

    def test_all_empty_strings(self): self.assertEqual(len_log(['', '', '']), 0)

    def test_words_with_spaces(self): self.assertEqual(len_log(['new york', 'LA', 'san francisco']), 13)

    def test_very_long_word(self): self.assertEqual(len_log(['a'*200, 'b'*150]), 200)

