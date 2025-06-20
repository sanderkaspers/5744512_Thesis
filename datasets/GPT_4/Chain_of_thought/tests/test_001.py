import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_remove_multiple_occurrences(self):
        self.assertEqual(remove_Occ('hello world', 'l'), 'heo word')

    def test_character_not_present(self):
        self.assertEqual(remove_Occ('hello world', 'x'), 'hello world')

    def test_all_characters_match(self):
        self.assertEqual(remove_Occ('aaaa', 'a'), '')

    def test_empty_string(self):
        self.assertEqual(remove_Occ('', 'a'), '')

    def test_empty_character(self):
        self.assertEqual(remove_Occ('hello', ''), 'hello')

    def test_single_character_match(self):
        self.assertEqual(remove_Occ('a', 'a'), '')

    def test_case_sensitivity(self):
        self.assertEqual(remove_Occ('Hello World', 'h'), 'Hello World')
        self.assertEqual(remove_Occ('Hello World', 'H'), 'ello World')

    def test_remove_special_character(self):
        self.assertEqual(remove_Occ('user@domain.com', '@'), 'userdomain.com')

    def test_unicode_character(self):
        self.assertEqual(remove_Occ('héllò', 'é'), 'hllò')

    def test_long_string(self):
        self.assertEqual(remove_Occ('a' * 1000, 'a'), '')

    def test_string_with_numbers(self):
        self.assertEqual(remove_Occ('12345', '3'), '1245')

    def test_character_at_start(self):
        self.assertEqual(remove_Occ('apple', 'a'), 'pple')

    def test_character_at_end(self):
        self.assertEqual(remove_Occ('banana', 'a'), 'bnn')

    def test_consecutive_characters(self):
        self.assertEqual(remove_Occ('bookkeeper', 'e'), 'bookkepr')

    def test_no_replacement_needed(self):
        self.assertEqual(remove_Occ('abcdef', 'x'), 'abcdef')

