import unittest
from datasets.GPT_4.Few_shot2.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_count_occurance_all_vowels_lowercase(self): self.assertEqual(count_occurance('aeiou'), 5)

    def test_count_occurance_all_vowels_uppercase(self): self.assertEqual(count_occurance('AEIOU'), 5)

    def test_count_occurance_mixed_vowels_and_consonants(self): self.assertEqual(count_occurance('Hello World'), 3)

    def test_count_occurance_no_vowels(self): self.assertEqual(count_occurance('bcdfg'), 0)

    def test_count_occurance_empty_string(self): self.assertEqual(count_occurance(''), 0)

    def test_count_occurance_only_spaces(self): self.assertEqual(count_occurance('     '), 0)

    def test_count_occurance_with_digits(self): self.assertEqual(count_occurance('h3ll0 w0rld'), 0)

    def test_count_occurance_mixed_case(self): self.assertEqual(count_occurance('ApPlE'), 2)

    def test_count_occurance_punctuation(self): self.assertEqual(count_occurance('!@#aeiou...'), 5)

