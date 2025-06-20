import unittest
from datasets.GPT_4.Few_shot2.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_find_even_pair_all_even(self): self.assertEqual(find_even_pair([2, 4, 6]), 3)

    def test_find_even_pair_all_odd(self): self.assertEqual(find_even_pair([1, 3, 5]), 3)

    def test_find_even_pair_mixed(self): self.assertEqual(find_even_pair([1, 2, 3, 4]), 2)

    def test_find_even_pair_no_pairs(self): self.assertEqual(find_even_pair([1]), 0)

    def test_find_even_pair_empty(self): self.assertEqual(find_even_pair([]), 0)

    def test_find_even_pair_repeated_values(self): self.assertEqual(find_even_pair([2, 2, 2]), 3)

    def test_find_even_pair_two_elements_even_sum(self): self.assertEqual(find_even_pair([4, 2]), 1)

    def test_find_even_pair_two_elements_odd_sum(self): self.assertEqual(find_even_pair([1, 2]), 0)

    def test_find_even_pair_large_input(self): self.assertEqual(find_even_pair([1]*50 + [2]*50), 1225)

