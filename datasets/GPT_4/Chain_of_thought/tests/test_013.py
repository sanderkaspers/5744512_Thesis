import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Substrings('1234'), 2)

    def test_single_digit(self):
        self.assertEqual(count_Substrings('5'), 0)

    def test_all_zeros(self):
        self.assertEqual(count_Substrings('000'), 3)

    def test_all_same_digit(self):
        self.assertEqual(count_Substrings('111'), 3)

    def test_alternating_digits(self):
        self.assertEqual(count_Substrings('1212'), 4)

    def test_increasing_sequence(self):
        self.assertEqual(count_Substrings('12345'), 3)

    def test_decreasing_sequence(self):
        self.assertEqual(count_Substrings('54321'), 3)

    def test_empty_string(self):
        self.assertEqual(count_Substrings(''), 0)

    def test_mixed_digit_lengths(self):
        self.assertEqual(count_Substrings('123456'), 5)

    def test_non_digit_characters(self):
        with self.assertRaises(ValueError):
            count_Substrings('12a34')

    def test_very_long_string(self):
        self.assertEqual(count_Substrings('1' * 1000), 1000)

    def test_boundary_condition_small_input(self):
        self.assertEqual(count_Substrings('9'), 0)

    def test_leading_zeros(self):
        self.assertEqual(count_Substrings('01234'), 2)

