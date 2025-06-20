import unittest
from datasets.GPT_4.Few_shot1.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_search_single_element(self): self.assertEqual(search([5]), 5)

    def test_search_duplicate_pairs(self): self.assertEqual(search([2, 3, 2, 3]), 0)

    def test_search_unique_among_duplicates(self): self.assertEqual(search([4, 1, 2, 1, 2]), 4)

    def test_search_multiple_unique_elements(self): self.assertEqual(search([1, 2, 3]), 0)

    def test_search_empty_list(self): self.assertEqual(search([]), 0)

    def test_search_large_values(self): self.assertEqual(search([1024, 1024, 2048]), 2048)

    def test_search_negatives(self): self.assertEqual(search([-1, -1, -2]), -2)

