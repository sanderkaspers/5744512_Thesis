import unittest
from datasets.GPT_4.Few_shot2.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_long_words_basic(self): self.assertEqual(long_words(3, 'The quick brown fox'), ['quick', 'brown'])

    def test_long_words_all_short(self): self.assertEqual(long_words(5, 'Hi to no yes'), [])

    def test_long_words_all_long(self): self.assertEqual(long_words(2, 'Hello world again'), ['Hello', 'world', 'again'])

    def test_long_words_empty_string(self): self.assertEqual(long_words(3, ''), [])

    def test_long_words_zero_threshold(self): self.assertEqual(long_words(0, 'a ab abc'), ['a', 'ab', 'abc'])

    def test_long_words_with_punctuation(self): self.assertEqual(long_words(3, 'Hi, this is GPT!'), ['this', 'GPT!'])

    def test_long_words_mixed_spacing(self): self.assertEqual(long_words(2, 'big  bear    bold'), ['big', 'bear', 'bold'])

    def test_long_words_threshold_equals_word(self): self.assertEqual(long_words(4, 'four foury'), ['foury'])

