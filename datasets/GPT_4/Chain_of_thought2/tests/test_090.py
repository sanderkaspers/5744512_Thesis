import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_all_correct_positions(self): self.assertEqual(count_char_position('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_some_correct_positions(self): self.assertEqual(count_char_position('aXcDefghijklmnopqrstuvwxyZ'), 21)

    def test_no_correct_positions(self): self.assertEqual(count_char_position('zzzzzzzzzzzzzzzzzzzzzzzzzz'), 0)

    def test_empty_string(self): self.assertEqual(count_char_position(''), 0)

    def test_single_matching_character(self): self.assertEqual(count_char_position('A'), 1)

    def test_single_non_matching_character(self): self.assertEqual(count_char_position('Z'), 0)

    def test_case_insensitivity(self): self.assertEqual(count_char_position('aBcDeFgHiJkLmNoPqRsTuVwXyZ'), 26)

    def test_string_with_non_letters(self): self.assertEqual(count_char_position('a1c$dE@gh!jkl#mnopqr'), 13)

    def test_longer_than_alphabet(self): self.assertEqual(count_char_position('abcdefghijklmnopqrstuvwxyz123'), 26)

    def test_non_letter_at_matching_position(self): self.assertEqual(count_char_position('a' + chr(ord('A') + 1) + '2'), 2)

