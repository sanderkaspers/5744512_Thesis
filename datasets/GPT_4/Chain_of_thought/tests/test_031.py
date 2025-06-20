import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Char('abc'), ord('f'))

    def test_empty_string(self):
        self.assertEqual(get_Char(''), ord('z'))

    def test_single_character(self):
        self.assertEqual(get_Char('d'), ord('d'))

    def test_all_characters_same(self):
        self.assertEqual(get_Char('aaa'), ord('c'))

    def test_max_ascii_characters(self):
        self.assertEqual(get_Char('xyz'), ord('u'))

    def test_min_ascii_characters(self):
        self.assertEqual(get_Char('abc'), ord('f'))

    def test_mixed_case_input(self):
        with self.assertRaises(ValueError):
            get_Char('AbC')

    def test_non_alphabetic_characters(self):
        with self.assertRaises(ValueError):
            get_Char('123')

    def test_long_string(self):
        self.assertEqual(get_Char('a' * 1000), ord('m'))

    def test_special_characters(self):
        with self.assertRaises(ValueError):
            get_Char('abc@!')

