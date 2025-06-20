import unittest
from datasets.GPT_4.Few_shot2.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_odd_values_string_basic(self): self.assertEqual(odd_values_string('abcdef'), 'bdf')

    def test_odd_values_string_odd_length(self): self.assertEqual(odd_values_string('abcde'), 'bd')

    def test_odd_values_string_even_length(self): self.assertEqual(odd_values_string('abcd'), 'bd')

    def test_odd_values_string_single_char(self): self.assertEqual(odd_values_string('a'), '')

    def test_odd_values_string_two_chars(self): self.assertEqual(odd_values_string('ab'), 'b')

    def test_odd_values_string_empty(self): self.assertEqual(odd_values_string(''), '')

    def test_odd_values_string_with_spaces(self): self.assertEqual(odd_values_string('a b c d'), '   ')

    def test_odd_values_string_with_symbols(self): self.assertEqual(odd_values_string('a!b@c#d$'), '!@#$')

    def test_odd_values_string_numerics(self): self.assertEqual(odd_values_string('1234567890'), '24680')

