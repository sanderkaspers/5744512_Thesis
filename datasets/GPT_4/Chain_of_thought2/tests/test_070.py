import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_words_longer_than_n(self): self.assertEqual(long_words(3, 'The quick brown fox'), ['quick', 'brown'])

    def test_no_words_longer_than_n(self): self.assertEqual(long_words(5, 'a an on the'), [])

    def test_all_words_longer_than_n(self): self.assertEqual(long_words(1, 'hi there hello'), ['hi', 'there', 'hello'])

    def test_n_equals_zero(self): self.assertEqual(long_words(0, 'a ab abc abcd'), ['a', 'ab', 'abc', 'abcd'])

    def test_n_equals_word_length(self): self.assertEqual(long_words(2, 'it is ok now'), [])

    def test_empty_string(self): self.assertEqual(long_words(2, ''), [])

    def test_with_punctuation(self): self.assertEqual(long_words(3, 'yes! wow. okay'), ['yes!', 'okay'])

    def test_mixed_case(self): self.assertEqual(long_words(2, 'Hi hi HI'), ['Hi', 'hi', 'HI'])

    def test_n_larger_than_all(self): self.assertEqual(long_words(10, 'short tiny minuscule'), [])

    def test_string_with_extra_spaces(self): self.assertEqual(long_words(2, '  many   spaces  here '), ['many', 'spaces', 'here'])

    def test_n_negative(self): self.assertEqual(long_words(-1, 'why not'), ['why', 'not'])

    def test_n_equals_length_boundary(self): self.assertEqual(long_words(4, 'four five six'), ['five'])

