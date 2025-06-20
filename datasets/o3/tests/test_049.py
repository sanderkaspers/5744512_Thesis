import unittest
from datasets.o3.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_k_middle(self):
        self.assertEqual(kth_element([3, 1, 2], 2), 2)

    def test_k_first(self):
        self.assertEqual(kth_element([3, 1, 2], 1), 1)

    def test_with_duplicates(self):
        self.assertEqual(kth_element([7, 7, 8, 1], 3), 7)

    def test_negative_numbers(self):
        self.assertEqual(kth_element([0, -1, -5], 2), -1)

    def test_k_last(self):
        self.assertEqual(kth_element([4, 6, 2, 5], 4), 6)

    def test_k_out_of_bounds(self):
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3], 4)

