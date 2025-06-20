import unittest
from datasets.GPT_4.Few_shot2.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_search_single_odd_occurrence(self): self.assertEqual(search([1, 1, 2]), 2)

    def test_search_basic_pair_and_one(self): self.assertEqual(search([4, 3, 4]), 3)

    def test_search_large_set_one_odd(self): self.assertEqual(search([7, 7, 5, 5, 8, 8, 9]), 9)

    def test_search_odd_in_middle(self): self.assertEqual(search([2, 3, 2]), 3)

    def test_search_with_zero(self): self.assertEqual(search([0, 1, 1]), 0)

    def test_search_negative_numbers(self): self.assertEqual(search([-1, -1, -2]), -2)

    def test_search_all_identical_odd_times(self): self.assertEqual(search([6]), 6)

    def test_search_multiple_even_one_odd(self): self.assertEqual(search([10, 20, 10, 30, 30, 20, 40]), 40)

