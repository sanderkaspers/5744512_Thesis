import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('1101', 4), 3)

    def test_all_zeros(self):
        self.assertEqual(odd_Equivalent('0000', 4), 0)

    def test_all_ones(self):
        self.assertEqual(odd_Equivalent('1111', 4), 4)

    def test_single_character(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_n_equals_length(self):
        self.assertEqual(odd_Equivalent('1101', 4), 3)

    def test_n_greater_than_length(self):
        self.assertEqual(odd_Equivalent('1101', 6), 3)

    def test_empty_string(self):
        self.assertEqual(odd_Equivalent('', 0), 0)

    def test_non_binary_string(self):
        with self.assertRaises(ValueError):
            odd_Equivalent('1102', 4)

    def test_n_equals_zero(self):
        self.assertEqual(odd_Equivalent('1101', 0), 0)

    def test_n_less_than_length(self):
        self.assertEqual(odd_Equivalent('1101', 2), 1)

