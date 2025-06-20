import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_all_odd_ascii(self): self.assertEqual(odd_Equivalent('ace', 2), 6)

    def test_all_even_ascii(self): self.assertEqual(odd_Equivalent('bd', 3), 0)

    def test_mixed_ascii(self): self.assertEqual(odd_Equivalent('abc', 1), 2)

    def test_empty_string(self): self.assertEqual(odd_Equivalent('', 10), 0)

    def test_multiplier_zero(self): self.assertEqual(odd_Equivalent('abcdef', 0), 0)

    def test_multiplier_one(self): self.assertEqual(odd_Equivalent('abc', 1), 2)

    def test_large_multiplier(self): self.assertEqual(odd_Equivalent('a', 1000), 1000)

    def test_whitespace_and_punctuation(self): self.assertEqual(odd_Equivalent(' !#', 1), 2)

    def test_string_with_digits(self): self.assertEqual(odd_Equivalent('1234', 1), 2)

    def test_negative_multiplier(self): self.assertEqual(odd_Equivalent('a', -2), -2)

    def test_unicode_characters(self): self.assertTrue(isinstance(odd_Equivalent('üß', 1), int))

