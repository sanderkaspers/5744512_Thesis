import unittest
from datasets.GPT_4.Few_shot1.programs.program_067 import *

class TestVersion(unittest.TestCase):
    def test_find_length_only_zeros(self): self.assertEqual(find_length("0000"), 4)

    def test_find_length_only_ones(self): self.assertEqual(find_length("1111"), 0)

    def test_find_length_mixed_balanced(self): self.assertEqual(find_length("0101"), 0)

    def test_find_length_more_zeros(self): self.assertEqual(find_length("0011"), 2)

    def test_find_length_alternating_start_zero(self): self.assertEqual(find_length("0101010"), 1)

    def test_find_length_alternating_start_one(self): self.assertEqual(find_length("1010101"), 0)

    def test_find_length_prefix_suffix_gain(self): self.assertEqual(find_length("11000011"), 2)

    def test_find_length_multiple_segments(self): self.assertEqual(find_length("1100000011"), 4)

    def test_find_length_empty_string(self): self.assertEqual(find_length(""), 0)

    def test_find_length_all_balanced(self): self.assertEqual(find_length("01011010"), 0)

