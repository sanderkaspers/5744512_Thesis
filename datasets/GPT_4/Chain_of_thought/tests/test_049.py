import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(kth_element([3, 1, 2], 2), 2)

    def test_k_equals_one(self):
        self.assertEqual(kth_element([5, 3, 1], 1), 1)

    def test_k_equals_length(self):
        self.assertEqual(kth_element([5, 3, 1], 3), 5)

    def test_k_larger_than_length(self):
        with self.assertRaises(IndexError):
            kth_element([5, 3, 1], 4)

    def test_array_with_duplicates(self):
        self.assertEqual(kth_element([4, 2, 4, 3], 3), 4)

    def test_array_with_negatives(self):
        self.assertEqual(kth_element([4, -2, 3, -1], 2), -1)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            kth_element([], 1)

    def test_single_element_array(self):
        self.assertEqual(kth_element([10], 1), 10)

    def test_unsorted_array(self):
        self.assertEqual(kth_element([3, 1, 4, 2], 4), 4)

    def test_non_integer_k(self):
        with self.assertRaises(TypeError):
            kth_element([1, 2, 3], '2')

