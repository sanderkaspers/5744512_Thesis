import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_even_length(self): self.assertEqual(odd_values_string('abcdef'), 'ace')

    def test_odd_length(self): self.assertEqual(odd_values_string('abcde'), 'ace')

    def test_one_char(self): self.assertEqual(odd_values_string('a'), 'a')

    def test_two_chars(self): self.assertEqual(odd_values_string('ab'), 'a')

    def test_repeated_chars(self): self.assertEqual(odd_values_string('aaaaaa'), 'aaa')

    def test_spaces_and_symbols(self): self.assertEqual(odd_values_string('a b.c!'), 'abc')

    def test_empty(self): self.assertEqual(odd_values_string(''), '')

    def test_unicode(self): self.assertEqual(odd_values_string('𝓪𝓫𝓬𝓭'), '𝓪𝓬')

    def test_digits(self): self.assertEqual(odd_values_string('123456789'), '13579')

    def test_newlines_and_tabs(self): self.assertEqual(odd_values_string('\na\tb\n'), '\na')

    def test_emojis(self): self.assertEqual(odd_values_string('🙂🙃😉😊'), '🙂😉')

