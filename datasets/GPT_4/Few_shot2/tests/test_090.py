import unittest
from datasets.GPT_4.Few_shot2.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_count_char_position_basic(self): self.assertEqual(count_char_position('a1b2c3'), 2)

    def test_count_char_position_all_alpha(self): self.assertEqual(count_char_position('abcdef'), 3)

    def test_count_char_position_all_non_alpha(self): self.assertEqual(count_char_position('123456'), 0)

    def test_count_char_position_empty(self): self.assertEqual(count_char_position(''), 0)

    def test_count_char_position_single_alpha(self): self.assertEqual(count_char_position('a'), 1)

    def test_count_char_position_single_non_alpha(self): self.assertEqual(count_char_position('1'), 0)

    def test_count_char_position_alpha_odd_indices(self): self.assertEqual(count_char_position('1a2b3c'), 0)

    def test_count_char_position_mixed_positions(self): self.assertEqual(count_char_position('1aB2cD3eF'), 2)

    def test_count_char_position_with_spaces(self): self.assertEqual(count_char_position('a b c d'), 2)

