import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_even_length_string(self): self.assertEqual(odd_values_string('abcdef'), 'ace')

    def test_odd_length_string(self): self.assertEqual(odd_values_string('abcde'), 'ace')

    def test_single_character(self): self.assertEqual(odd_values_string('x'), 'x')

    def test_all_same_characters(self): self.assertEqual(odd_values_string('aaaaaa'), 'aaa')

    def test_empty_string(self): self.assertEqual(odd_values_string(''), '')

    def test_with_numbers_and_symbols(self): self.assertEqual(odd_values_string('1!2@3#4$5%'), '12345')

    def test_mixed_case_string(self): self.assertEqual(odd_values_string('AbCdEf'), 'ACE')

    def test_palindrome_string(self): self.assertEqual(odd_values_string('racecar'), 'rcea')

    def test_unicode_characters(self): self.assertEqual(odd_values_string('àáâãäå'), 'àâä')

    def test_very_long_string(self): self.assertEqual(odd_values_string('a'*1000), 'a'*500)

