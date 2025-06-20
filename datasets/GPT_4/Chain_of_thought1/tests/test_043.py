import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_mixed_lengths(self): self.assertEqual(Find_Min_Length(['apple', 'pie', 'hi', 'no']), ['hi', 'no'])

    def test_all_same_length(self): self.assertEqual(Find_Min_Length(['aa', 'bb', 'cc']), ['aa', 'bb', 'cc'])

    def test_single_string(self): self.assertEqual(Find_Min_Length(['hello']), ['hello'])

    def test_contains_empty_string(self): self.assertEqual(Find_Min_Length(['', 'a', 'bb']), [''])

    def test_all_empty_strings(self): self.assertEqual(Find_Min_Length(['', '', '']), ['', '', ''])

    def test_duplicates_of_shortest(self): self.assertEqual(Find_Min_Length(['a', 'abc', 'a', 'de']), ['a', 'a'])

    def test_tied_min_strings(self): self.assertEqual(Find_Min_Length(['foo', 'bar', 'hi', 'ok']), ['hi', 'ok'])

    def test_numeric_strings(self): self.assertEqual(Find_Min_Length(['123', '4', '56']), ['4'])

