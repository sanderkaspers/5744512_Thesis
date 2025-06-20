import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_simple_case(self): self.assertEqual(search([1, 1, 2]), 2)

    def test_single_element(self): self.assertEqual(search([7]), 7)

    def test_large_case(self): self.assertEqual(search([10, 10, 5, 5, 6]), 6)

    def test_negative_numbers(self): self.assertEqual(search([-1, -1, -2]), -2)

    def test_zero_odd(self): self.assertEqual(search([0, 1, 1]), 0)

    def test_one_outlier(self): self.assertEqual(search([2, 2, 2, 2, 3]), 3)

    def test_odd_at_start(self): self.assertEqual(search([9, 1, 1, 2, 2]), 9)

    def test_odd_at_end(self): self.assertEqual(search([1, 1, 2, 2, 9]), 9)

    def test_same_repeated_odd(self): self.assertEqual(search([4, 4, 4, 4, 4]), 4)

    def test_large_numbers(self): self.assertEqual(search([10**6, 10**6, 999999]), 999999)

    def test_all_even(self): self.assertEqual(search([1, 1, 2, 2]), 0)

    def test_empty_list(self): self.assertEqual(search([]), 0)

    def test_multiple_odds(self): self.assertNotEqual(search([1, 2, 3]), 1)

