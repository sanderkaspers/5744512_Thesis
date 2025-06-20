import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_unique_lengths(self): self.assertEqual(len_log(['a', 'ab', 'abc', 'abcd']), 'abcd')

    def test_tied_max_length(self): self.assertEqual(len_log(['first', 'second', 'thirds']), 'thirds')

    def test_same_length(self): self.assertEqual(len_log(['aa', 'bb', 'cc']), 'aa')

    def test_single_string(self): self.assertEqual(len_log(['hello']), 'hello')

    def test_with_empty_strings(self): self.assertEqual(len_log(['', 'a', '', 'abc', 'ab']), 'abc')

    def test_single_empty_string(self): self.assertEqual(len_log(['']), '')

