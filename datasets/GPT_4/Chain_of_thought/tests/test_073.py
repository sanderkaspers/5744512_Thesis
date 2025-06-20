import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_vowels('hello world'), 'hollo werld')

    def test_no_vowels(self):
        self.assertEqual(reverse_vowels('bcdfgh'), 'bcdfgh')

    def test_only_vowels(self):
        self.assertEqual(reverse_vowels('aeiou'), 'uoiea')

    def test_mixed_case_vowels(self):
        self.assertEqual(reverse_vowels('HeLlO WoRlD'), 'HoLlE WeRlD')

    def test_single_vowel(self):
        self.assertEqual(reverse_vowels('a'), 'a')

    def test_spaces_and_punctuation(self):
        self.assertEqual(reverse_vowels('hello, world!'), 'holle, werld!')

    def test_consecutive_vowels(self):
        self.assertEqual(reverse_vowels('see you'), 'soe yee')

    def test_digits_and_special_characters(self):
        self.assertEqual(reverse_vowels('h3ll0 w0rld!'), 'h3ll0 w0rld!')

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(''), '')

    def test_very_long_string(self):
        long_string = 'a' * 10000 + 'e' * 10000
        reversed_string = 'e' * 10000 + 'a' * 10000
        self.assertEqual(reverse_vowels(long_string), reversed_string)

