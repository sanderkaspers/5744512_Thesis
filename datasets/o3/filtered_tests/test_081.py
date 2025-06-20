import unittest
from datasets.o3.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_pancake_sort_already_sorted(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_pancake_sort_reverse(self):
        self.assertEqual(pancake_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_pancake_sort_duplicates(self):
        self.assertEqual(pancake_sort([3, 1, 3, 2]), [1, 2, 3, 3])

    def test_pancake_sort_empty(self):
        self.assertEqual(pancake_sort([]), [])

    def test_pancake_sort_single_element(self):
        self.assertEqual(pancake_sort([42]), [42])

    def test_pancake_sort_negative_numbers(self):
        self.assertEqual(pancake_sort([-3, -1, -2]), [-3, -2, -1])

    def test_pancake_sort_mixed_floats(self):
        self.assertEqual(pancake_sort([3.5, 2.2, 3.5, 1.1]), [1.1, 2.2, 3.5, 3.5])

