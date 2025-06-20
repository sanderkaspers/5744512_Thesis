import unittest
from datasets.GPT_4.Few_shot2.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_duplicate_with_duplicates(self): self.assertTrue(test_duplicate([1, 2, 3, 2]))

    def test_duplicate_no_duplicates(self): self.assertFalse(test_duplicate([1, 2, 3, 4]))

    def test_duplicate_empty_list(self): self.assertFalse(test_duplicate([]))

    def test_duplicate_single_element(self): self.assertFalse(test_duplicate([1]))

    def test_duplicate_all_same(self): self.assertTrue(test_duplicate([7, 7, 7, 7]))

    def test_duplicate_with_strings(self): self.assertTrue(test_duplicate(['a', 'b', 'a']))

    def test_duplicate_strings_no_duplicates(self): self.assertFalse(test_duplicate(['a', 'b', 'c']))

    def test_duplicate_mixed_types(self): self.assertTrue(test_duplicate([1, '1', 1]))

    def test_duplicate_large_list(self): self.assertFalse(test_duplicate(list(range(10000))))

    def test_duplicate_large_list_with_duplicate(self): self.assertTrue(test_duplicate(list(range(10000)) + [9999]))

