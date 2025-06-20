import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_char_position('abcxyz'), 3)

    def test_all_in_position(self):
        self.assertEqual(count_char_position('abcdef'), 6)

    def test_no_in_position(self):
        self.assertEqual(count_char_position('zyxwvu'), 0)

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_single_char_in_position(self):
        self.assertEqual(count_char_position('a'), 1)

    def test_single_char_not_in_position(self):
        self.assertEqual(count_char_position('b'), 0)

    def test_mixed_case(self):
        self.assertEqual(count_char_position('AbC'), 3)

    def test_non_alphabetic_chars(self):
        self.assertEqual(count_char_position('a1c!'), 2)

    def test_long_string(self):
        long_string = 'abcdefghijklmnopqrstuvwxyz' * 1000
        self.assertEqual(count_char_position(long_string), 26000)

    def test_repeated_chars(self):
        self.assertEqual(count_char_position('aaa'), 1)

