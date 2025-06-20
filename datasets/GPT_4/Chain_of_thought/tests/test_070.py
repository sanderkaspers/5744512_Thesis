import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(long_words(3, 'This is a test string'), ['This', 'test', 'string'])

    def test_all_words_shorter_than_n(self):
        self.assertEqual(long_words(5, 'a bb ccc dddd'), [])

    def test_all_words_longer_than_n(self):
        self.assertEqual(long_words(1, 'longer words here'), ['longer', 'words', 'here'])

    def test_exact_length_match(self):
        self.assertEqual(long_words(4, 'This is a test'), [])

    def test_empty_string(self):
        self.assertEqual(long_words(4, ''), [])

    def test_special_characters(self):
        self.assertEqual(long_words(3, 'hello @world #hashtag $money'), ['hello', '@world', '#hashtag', '$money'])

    def test_numbers_in_string(self):
        self.assertEqual(long_words(3, 'word1 word2 word3 1234'), ['word1', 'word2', 'word3', '1234'])

    def test_punctuation_in_string(self):
        self.assertEqual(long_words(3, 'hello, world! test.'), ['hello,', 'world!', 'test.'])

    def test_multiple_spaces_in_string(self):
        self.assertEqual(long_words(3, 'word1  word2   word3'), ['word1', 'word2', 'word3'])

    def test_mixed_case_words(self):
        self.assertEqual(long_words(3, 'This is A Test STRING'), ['This', 'Test', 'STRING'])

