import unittest
from datasets.GPT_4.Few_shot2.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_reverse_vowels_basic(self): self.assertEqual(reverse_vowels('hello'), 'holle')

    def test_reverse_vowels_uppercase(self): self.assertEqual(reverse_vowels('HELLO'), 'HOLLE')

    def test_reverse_vowels_mixed_case(self): self.assertEqual(reverse_vowels('HeLLo'), 'HoLLe')

    def test_reverse_vowels_all_vowels(self): self.assertEqual(reverse_vowels('aeiou'), 'uoiea')

    def test_reverse_vowels_no_vowels(self): self.assertEqual(reverse_vowels('bcdfg'), 'bcdfg')

    def test_reverse_vowels_single_vowel(self): self.assertEqual(reverse_vowels('xay'), 'xay')

    def test_reverse_vowels_empty_string(self): self.assertEqual(reverse_vowels(''), '')

    def test_reverse_vowels_repeated_vowels(self): self.assertEqual(reverse_vowels('aabbccddaa'), 'aabbccddaa')

    def test_reverse_vowels_with_spaces(self): self.assertEqual(reverse_vowels('a e i o u'), 'u o i e a')

    def test_reverse_vowels_with_punctuation(self): self.assertEqual(reverse_vowels('h!e?l.l,o'), 'h!o?l.l,e')

