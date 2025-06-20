import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_multiple_occurrences(self): self.assertEqual(remove_Occ('banana', 'a'), 'bnn')

    def test_single_occurrence(self): self.assertEqual(remove_Occ('apple', 'p'), 'ale')

    def test_character_not_present(self): self.assertEqual(remove_Occ('hello', 'z'), 'hello')

    def test_empty_string(self): self.assertEqual(remove_Occ('', 'a'), '')

    def test_empty_character(self): self.assertEqual(remove_Occ('text', ''), 'text')

    def test_string_of_character(self): self.assertEqual(remove_Occ('aaaaa', 'a'), '')

    def test_case_sensitivity(self): self.assertEqual(remove_Occ('ApplE', 'a'), 'ApplE')

    def test_remove_digit(self): self.assertEqual(remove_Occ('abc123abc', '1'), 'abc23abc')

    def test_remove_punctuation(self): self.assertEqual(remove_Occ('hello, world!', ','), 'hello world!')

    def test_remove_space(self): self.assertEqual(remove_Occ('remove all spaces', ' '), 'removeallspaces')

    def test_unicode_emoji(self): self.assertEqual(remove_Occ('😀a😀b😀', '😀'), 'ab')

    def test_repeating_pattern(self): self.assertEqual(remove_Occ('abababab', 'b'), 'aaaa')

