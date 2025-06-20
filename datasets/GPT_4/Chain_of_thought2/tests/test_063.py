import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_unique_at_end(self): self.assertEqual(search([1, 1, 2, 2, 3]), 3)

    def test_unique_at_start(self): self.assertEqual(search([4, 5, 5, 6, 6]), 4)

    def test_unique_in_middle(self): self.assertEqual(search([7, 7, 8, 9, 9]), 8)

    def test_single_element(self): self.assertEqual(search([42]), 42)

    def test_with_negative_numbers(self): self.assertEqual(search([-1, -1, 0, 1, 1]), 0)

    def test_with_zero(self): self.assertEqual(search([0, 0, 99]), 99)

    def test_large_numbers(self): self.assertEqual(search([999999, 888888, 999999]), 888888)

    def test_multiple_unique_elements(self): result = search([1, 2, 3]); self.assertIsInstance(result, int)

    def test_all_duplicates(self): self.assertEqual(search([10, 10]), 0)

