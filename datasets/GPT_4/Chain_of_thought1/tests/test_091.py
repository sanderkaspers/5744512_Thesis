import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_all_even(self): self.assertEqual(find_even_pair([2, 4, 6]), 3)

    def test_all_odd(self): self.assertEqual(find_even_pair([1, 3, 5]), 3)

    def test_mixed_parity(self): self.assertEqual(find_even_pair([1, 2, 3]), 1)

    def test_no_even_xor(self): self.assertEqual(find_even_pair([1, 2]), 0)

    def test_one_element(self): self.assertEqual(find_even_pair([5]), 0)

    def test_empty_list(self): self.assertEqual(find_even_pair([]), 0)

    def test_duplicate_elements(self): self.assertEqual(find_even_pair([2, 2, 2]), 3)

    def test_negative_values(self): self.assertEqual(find_even_pair([-2, -4]), 1)

    def test_large_input(self): result = find_even_pair(list(range(100))); self.assertIsInstance(result, int)

