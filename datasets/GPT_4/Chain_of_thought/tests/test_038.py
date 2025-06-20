import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(len_log(['apple', 'banana', 'cherry', 'date']), 6)

    def test_all_same_length(self):
        self.assertEqual(len_log(['dog', 'cat', 'bat']), 3)

    def test_single_word(self):
        self.assertEqual(len_log(['elephant']), 8)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            len_log([])

    def test_special_characters(self):
        self.assertEqual(len_log(['hello!', 'hi', '@home', '#hashtag']), 8)

    def test_mixed_case_words(self):
        self.assertEqual(len_log(['Python', 'javaScript', 'HTML']), 10)

    def test_numeric_strings(self):
        self.assertEqual(len_log(['1234', '56789', '0']), 5)

    def test_very_long_word(self):
        long_word = 'a' * 1000
        self.assertEqual(len_log([long_word, 'short']), 1000)

    def test_words_with_spaces(self):
        self.assertEqual(len_log(['new york', 'san francisco', 'los angeles']), 13)

