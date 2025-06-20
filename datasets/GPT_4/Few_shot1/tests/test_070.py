import unittest
from datasets.GPT_4.Few_shot1.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_long_words_basic(self): self.assertEqual(long_words(3, "this is a test"), ["this", "test"])

    def test_long_words_all_short(self): self.assertEqual(long_words(5, "cat dog sun"), [])

    def test_long_words_all_long(self): self.assertEqual(long_words(2, "apple banana cherry"), ["apple", "banana", "cherry"])

    def test_long_words_empty_string(self): self.assertEqual(long_words(3, ""), [])

    def test_long_words_no_spaces(self): self.assertEqual(long_words(3, "hello"), ["hello"])

    def test_long_words_threshold_edge(self): self.assertEqual(long_words(4, "frog leap frogger"), ["frogger"])

    def test_long_words_with_punctuation(self): self.assertEqual(long_words(3, "hi! you, there."), ["there."])

    def test_long_words_mixed_cases(self): self.assertEqual(long_words(2, "Hi HI hi hI"), ["Hi", "HI", "hi", "hI"])

    def test_long_words_large_threshold(self): self.assertEqual(long_words(10, "short words only"), [])

    def test_long_words_n_zero(self): self.assertEqual(long_words(0, "one two three"), ["one", "two", "three"])

