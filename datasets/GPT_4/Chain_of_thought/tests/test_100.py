import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

    def test_single_character(self):
        self.assertEqual(odd_values_string('a'), 'a')

    def test_two_characters(self):
        self.assertEqual(odd_values_string('ab'), 'a')

    def test_even_indices(self):
        self.assertEqual(odd_values_string('aceg'), 'aceg')

    def test_odd_indices(self):
        self.assertEqual(odd_values_string('bdfh'), 'bdh')

    def test_empty_string(self):
        self.assertEqual(odd_values_string(''), '')

    def test_special_characters(self):
        self.assertEqual(odd_values_string('a!b@c#d$'), 'a@#$')

    def test_mixed_case(self):
        self.assertEqual(odd_values_string('AbCdEf'), 'ACE')

    def test_string_with_numbers(self):
        self.assertEqual(odd_values_string('a1b2c3d4'), 'abcd')

    def test_very_long_string(self):
        long_string = 'a' * 1000 + 'b' * 1000
        self.assertEqual(odd_values_string(long_string), 'a' * 1000)

