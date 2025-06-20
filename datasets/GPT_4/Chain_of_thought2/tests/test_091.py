import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_all_even(self): self.assertEqual(find_even_pair([2, 4, 6, 8]), 6)

    def test_all_odd(self): self.assertEqual(find_even_pair([1, 3, 5]), 3)

    def test_mixed_even_odd(self): self.assertEqual(find_even_pair([1, 2, 3, 4]), 2)

    def test_single_element(self): self.assertEqual(find_even_pair([1]), 0)

    def test_repeated_values(self): self.assertEqual(find_even_pair([2, 2, 2]), 3)

    def test_empty_list(self): self.assertEqual(find_even_pair([]), 0)

    def test_even_and_odd_no_pair(self): self.assertEqual(find_even_pair([2, 3]), 0)

    def test_large_same_value(self): self.assertEqual(find_even_pair([4]*10), 45)

    def test_negative_numbers_even_result(self): self.assertEqual(find_even_pair([-2, -4]), 1)

    def test_large_range(self): self.assertEqual(find_even_pair(list(range(20))), 90)

