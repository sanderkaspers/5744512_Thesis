import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_no_duplicates(self): self.assertFalse(test_duplicate([1, 2, 3, 4, 5]))

    def test_single_duplicate(self): self.assertTrue(test_duplicate([1, 2, 3, 2]))

    def test_multiple_duplicates(self): self.assertTrue(test_duplicate([1, 2, 2, 3, 3, 4]))

    def test_all_same_elements(self): self.assertTrue(test_duplicate([9, 9, 9, 9]))

    def test_empty_list(self): self.assertFalse(test_duplicate([]))

    def test_single_element(self): self.assertFalse(test_duplicate([42]))

    def test_int_float_equivalence(self): self.assertTrue(test_duplicate([1, 1.0]))

    def test_negative_numbers(self): self.assertFalse(test_duplicate([-1, -2, -3, -4]))

    def test_large_unique_list(self): self.assertFalse(test_duplicate(list(range(10000))))

