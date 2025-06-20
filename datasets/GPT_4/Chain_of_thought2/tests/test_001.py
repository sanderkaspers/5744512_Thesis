import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_single_occurrence(self): self.assertEqual(remove_Occ("apple", "a"), "pple")

    def test_multiple_non_consecutive(self): self.assertEqual(remove_Occ("banana", "a"), "bnn")

    def test_multiple_consecutive(self): self.assertEqual(remove_Occ("aabbcc", "a"), "bbcc")

    def test_character_not_in_string(self): self.assertEqual(remove_Occ("hello", "z"), "hello")

    def test_empty_string(self): self.assertEqual(remove_Occ("", "x"), "")

    def test_empty_character(self): self.assertEqual(remove_Occ("hello", ""), "hello")

    def test_case_sensitivity(self): self.assertEqual(remove_Occ("Apple", "a"), "Apple")

    def test_all_target_characters(self): self.assertEqual(remove_Occ("aaaa", "a"), "")

    def test_long_string(self): s = "x"*1000 + "y"*1000; expected = "y"*1000; self.assertEqual(remove_Occ(s, "x"), expected)

    def test_special_character(self): self.assertEqual(remove_Occ("he!llo!wo!rld!", "!"), "helloworld")

    def test_unicode_removal(self): self.assertEqual(remove_Occ("café☕coffee☕", "☕"), "cafécoffee")

