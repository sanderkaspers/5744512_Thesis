import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_typical_valid_case(self):
        self.assertTrue(text_lowercase_underscore('abc_def'))

    def test_no_underscore(self):
        self.assertFalse(text_lowercase_underscore('abcdef'))

    def test_multiple_underscores(self):
        self.assertFalse(text_lowercase_underscore('abc_def_ghi'))

    def test_leading_underscore(self):
        self.assertFalse(text_lowercase_underscore('_abcdef'))

    def test_trailing_underscore(self):
        self.assertFalse(text_lowercase_underscore('abcdef_'))

    def test_uppercase_letters(self):
        self.assertFalse(text_lowercase_underscore('Abc_Def'))

    def test_mixed_case_letters(self):
        self.assertFalse(text_lowercase_underscore('abc_DeF'))

    def test_numbers_in_string(self):
        self.assertFalse(text_lowercase_underscore('abc_123'))

    def test_special_characters_in_string(self):
        self.assertFalse(text_lowercase_underscore('abc_@#$'))

    def test_empty_string(self):
        self.assertFalse(text_lowercase_underscore(''))

    def test_single_letter_strings(self):
        self.assertTrue(text_lowercase_underscore('a_b'))
        self.assertFalse(text_lowercase_underscore('a_'))

    def test_multiple_sequences(self):
        self.assertFalse(text_lowercase_underscore('abc_def_ghi'))

    def test_exact_match(self):
        self.assertTrue(text_lowercase_underscore('abc_def'))

    def test_long_valid_string(self):
        self.assertTrue(text_lowercase_underscore('a' * 100 + '_' + 'b' * 100))

    def test_long_invalid_string(self):
        self.assertFalse(text_lowercase_underscore('a' * 100 + '_' + 'B' * 100))

    def test_invalid_input_integer(self):
        with self.assertRaises(TypeError):
            text_lowercase_underscore(123)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            text_lowercase_underscore(['abc_def'])

    def test_case_sensitivity(self):
        self.assertFalse(text_lowercase_underscore('abc_DEF'))

    def test_special_characters_with_underscores(self):
        self.assertFalse(text_lowercase_underscore('abc_@#$_def'))

