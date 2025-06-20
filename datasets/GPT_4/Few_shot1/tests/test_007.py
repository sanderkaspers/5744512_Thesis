import unittest
from datasets.GPT_4.Few_shot1.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_duplicate_empty_list(self): self.assertEqual(test_duplicate([]), False)

    def test_duplicate_single_element(self): self.assertEqual(test_duplicate([1]), False)

    def test_duplicate_no_duplicates(self): self.assertEqual(test_duplicate([1, 2, 3, 4, 5]), False)

    def test_duplicate_one_duplicate(self): self.assertEqual(test_duplicate([1, 2, 3, 2]), True)

    def test_duplicate_multiple_duplicates(self): self.assertEqual(test_duplicate([1, 2, 3, 1, 2]), True)

    def test_duplicate_all_same(self): self.assertEqual(test_duplicate([7, 7, 7, 7]), True)

    def test_duplicate_with_strings(self): self.assertEqual(test_duplicate(["a", "b", "c", "a"]), True)

    def test_duplicate_mixed_types(self): self.assertEqual(test_duplicate([1, "1", 1.0]), True)

    def test_duplicate_large_input(self): self.assertEqual(test_duplicate(list(range(10000)) + [0]), True)

    def test_duplicate_with_none(self): self.assertEqual(test_duplicate([None, None]), True)

