import unittest
from datasets.GPT_4.Few_shot1.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_even_pair_empty(self): self.assertEqual(find_even_pair([]), 0)

    def test_even_pair_single_element(self): self.assertEqual(find_even_pair([2]), 0)

    def test_even_pair_two_even(self): self.assertEqual(find_even_pair([2, 4]), 1)

    def test_even_pair_two_odd(self): self.assertEqual(find_even_pair([1, 3]), 1)

    def test_even_pair_even_and_odd(self): self.assertEqual(find_even_pair([2, 3]), 0)

    def test_even_pair_all_even(self): self.assertEqual(find_even_pair([2, 4, 6]), 3)

    def test_even_pair_all_odd(self): self.assertEqual(find_even_pair([1, 3, 5]), 3)

    def test_even_pair_mixed(self): self.assertEqual(find_even_pair([1, 2, 3, 4]), 2)

    def test_even_pair_alternating(self): self.assertEqual(find_even_pair([1, 2, 3, 4, 5, 6]), 6)

    def test_even_pair_large_even_block(self): self.assertEqual(find_even_pair([2]*10), 45)

    def test_even_pair_large_odd_block(self): self.assertEqual(find_even_pair([1]*10), 45)

    def test_even_pair_large_mixed(self): self.assertEqual(find_even_pair([1, 2]*5), 10)

    def test_even_pair_duplicates(self): self.assertEqual(find_even_pair([2, 2, 2]), 3)

    def test_even_pair_negatives(self): self.assertEqual(find_even_pair([-1, -3, -5]), 3)

    def test_even_pair_neg_even_and_pos_even(self): self.assertEqual(find_even_pair([-2, 4]), 1)

