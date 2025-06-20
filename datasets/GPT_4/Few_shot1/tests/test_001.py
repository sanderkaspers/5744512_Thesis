import unittest
from datasets.GPT_4.Few_shot1.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_remove_occ_empty_string(self): self.assertEqual(remove_Occ("", 'a'), "")

    def test_remove_occ_char_not_in_string(self): self.assertEqual(remove_Occ("hello", 'x'), "hello")

    def test_remove_occ_single_occurrence(self): self.assertEqual(remove_Occ("hello", 'e'), "hllo")

    def test_remove_occ_multiple_occurrences(self): self.assertEqual(remove_Occ("banana", 'a'), "bnn")

    def test_remove_occ_all_characters_match(self): self.assertEqual(remove_Occ("aaa", 'a'), "")

    def test_remove_occ_case_sensitivity(self): self.assertEqual(remove_Occ("AbcA", 'a'), "AbcA")

    def test_remove_occ_digit_character(self): self.assertEqual(remove_Occ("a1b2c3", '2'), "a1bc3")

    def test_remove_occ_special_character(self): self.assertEqual(remove_Occ("hello!", '!'), "hello")

    def test_remove_occ_whitespace(self): self.assertEqual(remove_Occ("hello world", ' '), "helloworld")

    def test_remove_occ_first_and_last(self): self.assertEqual(remove_Occ("abca", 'a'), "bc")

