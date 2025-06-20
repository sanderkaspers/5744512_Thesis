import unittest
from datasets.GPT_4.Few_shot1.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_kth_element_basic(self): self.assertEqual(kth_element([3, 1, 2], 2), 2)

    def test_kth_element_first(self): self.assertEqual(kth_element([4, 2, 5, 1], 1), 1)

    def test_kth_element_last(self): self.assertEqual(kth_element([4, 2, 5, 1], 4), 5)

    def test_kth_element_duplicates(self): self.assertEqual(kth_element([5, 3, 3, 3, 1], 2), 3)

    def test_kth_element_single(self): self.assertEqual(kth_element([42], 1), 42)

    def test_kth_element_sorted_input(self): self.assertEqual(kth_element([1, 2, 3, 4], 3), 3)

    def test_kth_element_reverse_sorted(self): self.assertEqual(kth_element([9, 7, 5, 3], 2), 5)

