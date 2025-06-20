import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_067 import *

class TestVersion(unittest.TestCase):
    def test_all_zeros(self): self.assertEqual(find_length('00000'), 5)

    def test_all_ones(self): self.assertEqual(find_length('11111'), 0)

    def test_equal_zeros_ones(self): self.assertEqual(find_length('010101'), 1)

    def test_more_zeros_than_ones(self): self.assertEqual(find_length('001001'), 3)

    def test_more_ones_than_zeros(self): self.assertEqual(find_length('1101001'), 2)

    def test_alternating(self): self.assertEqual(find_length('010101010'), 1)

    def test_longest_substring_in_middle(self): self.assertEqual(find_length('1110000111'), 4)

    def test_longest_substring_at_end(self): self.assertEqual(find_length('110000'), 4)

    def test_empty_string(self): self.assertEqual(find_length(''), 0)

    def test_single_zero(self): self.assertEqual(find_length('0'), 1)

    def test_single_one(self): self.assertEqual(find_length('1'), 0)

    def test_non_binary_input(self): self.assertEqual(find_length('0a1b0'), 1)

    def test_large_balanced_pattern(self): self.assertEqual(find_length('01' * 1000), 1)

