import unittest
from datasets.GPT_4.Few_shot2.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_kth_element_basic(self): self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 3), 7)

    def test_kth_element_sorted_array(self): self.assertEqual(kth_element([1, 2, 3, 4, 5], 2), 2)

    def test_kth_element_reverse_sorted(self): self.assertEqual(kth_element([5, 4, 3, 2, 1], 4), 4)

    def test_kth_element_k_is_one(self): self.assertEqual(kth_element([8, 6, 7, 5], 1), 5)

    def test_kth_element_k_equals_length(self): self.assertEqual(kth_element([3, 1, 4, 1, 5], 5), 5)

    def test_kth_element_with_duplicates(self): self.assertEqual(kth_element([1, 1, 2, 2, 3], 3), 2)

    def test_kth_element_all_same(self): self.assertEqual(kth_element([9, 9, 9], 2), 9)

    def test_kth_element_large_k(self): self.assertEqual(kth_element([10, 30, 20, 40, 50], 5), 50)

