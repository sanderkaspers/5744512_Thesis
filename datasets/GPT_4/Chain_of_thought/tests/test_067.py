import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_067 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_length('110100110'), 2)

    def test_all_zeros(self):
        self.assertEqual(find_length('00000'), 5)

    def test_all_ones(self):
        self.assertEqual(find_length('11111'), 0)

    def test_alternating_zeros_ones(self):
        self.assertEqual(find_length('010101'), 1)

    def test_empty_string(self):
        self.assertEqual(find_length(''), 0)

    def test_substrings_of_zeros_ones(self):
        self.assertEqual(find_length('000111000'), 3)

    def test_single_character_string(self):
        self.assertEqual(find_length('0'), 1)
        self.assertEqual(find_length('1'), 0)

    def test_leading_trailing_zeros(self):
        self.assertEqual(find_length('0011100'), 2)

    def test_mixed_length_substrings(self):
        self.assertEqual(find_length('000110011'), 3)

    def test_very_long_binary_string(self):
        long_string = '0' * 10000 + '1' * 10000
        self.assertEqual(find_length(long_string), 10000)

