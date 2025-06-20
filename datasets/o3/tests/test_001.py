import unittest
from datasets.o3.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_remove_single_occurrence(self):
        self.assertEqual(remove_Occ("banana", "b"), "anana")

    def test_remove_multiple_occurrences(self):
        self.assertEqual(remove_Occ("mississippi", "s"), "miippi")

    def test_remove_char_not_present(self):
        self.assertEqual(remove_Occ("hello", "x"), "hello")

    def test_remove_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_remove_special_character(self):
        self.assertEqual(remove_Occ("café", "é"), "caf")

    def test_case_sensitive(self):
        self.assertEqual(remove_Occ("Apple", "a"), "Apple")

