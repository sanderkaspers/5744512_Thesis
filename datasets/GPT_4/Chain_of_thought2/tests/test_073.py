import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_basic_vowel_reversal(self): self.assertEqual(reverse_vowels('hello'), 'holle')

    def test_no_vowels(self): self.assertEqual(reverse_vowels('rhythm'), 'rhythm')

    def test_all_vowels(self): self.assertEqual(reverse_vowels('aeiou'), 'uoiea')

    def test_mixed_case_vowels(self): self.assertEqual(reverse_vowels('hEllO'), 'hOllE')

    def test_start_end_vowels(self): self.assertEqual(reverse_vowels('apple'), 'eppla')

    def test_vowels_next_to_each_other(self): self.assertEqual(reverse_vowels('boot'), 'toob')

    def test_empty_string(self): self.assertEqual(reverse_vowels(''), '')

    def test_single_character_vowel(self): self.assertEqual(reverse_vowels('a'), 'a')

    def test_single_character_consonant(self): self.assertEqual(reverse_vowels('z'), 'z')

    def test_y_is_not_vowel(self): self.assertEqual(reverse_vowels('yoyo'), 'yoyo')

    def test_with_spaces_and_symbols(self): self.assertEqual(reverse_vowels('a!e@i#o$u%'), 'u!o@i#e$a%')

