import unittest
from datasets.GPT_4.Few_shot1.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_char_position_all_match_lowercase(self): self.assertEqual(count_char_position("abcdefghijklmnopqrstuvwxyz"), 1)

    def test_char_position_all_match_uppercase(self): self.assertEqual(count_char_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 1)

    def test_char_position_some_match(self): self.assertEqual(count_char_position("AbCdEfGhIj"), 2)

    def test_char_position_empty_string(self): self.assertEqual(count_char_position(""), 0)

    def test_char_position_single_match(self): self.assertEqual(count_char_position("A"), 1)

    def test_char_position_single_no_match(self): self.assertEqual(count_char_position("B"), 0)

    def test_char_position_repeated_match(self): self.assertEqual(count_char_position("A" * 26), 1)

    def test_char_position_mixed_chars(self): self.assertEqual(count_char_position("A1!a2@Zz"), 2)

    def test_char_position_case_sensitive(self): self.assertEqual(count_char_position("Aa"), 2)

    def test_char_position_non_alpha(self): self.assertEqual(count_char_position("1234567890!@#"), 0)

    def test_char_position_last_index_match(self):
        s = ['a'] * 122
        s[97] = 'a'
        self.assertEqual(count_char_position(''.join(s)), 1)

    def test_char_position_middle_match(self):
        s = ['b'] * 100
        s[98] = 'b'
        self.assertEqual(count_char_position(''.join(s)), 1)

    def test_char_position_multiple_valid_indices(self):
        s = ['a'] * 26
        for i in range(26): s[i] = chr(ord('a') + i)
        self.assertEqual(count_char_position(''.join(s)), 1)

    def test_char_position_large_string_no_match(self): self.assertEqual(count_char_position("z" * 1000), 0)

    def test_char_position_large_string_some_match(self):
        s = list("z" * 1000)
        s[25] = 'z'
        self.assertEqual(count_char_position(''.join(s)), 1)

