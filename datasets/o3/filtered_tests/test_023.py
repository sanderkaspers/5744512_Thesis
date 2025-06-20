import unittest
from datasets.o3.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element(self):
        self.assertEqual(comb_sort([42]), [42])

    def test_already_sorted(self):
        self.assertEqual(comb_sort([1,2,3,4]), [1,2,3,4])

    def test_reverse_sorted(self):
        self.assertEqual(comb_sort([4,3,2,1]), [1,2,3,4])

    def test_duplicates(self):
        self.assertEqual(comb_sort([3,1,2,3]), [1,2,3,3])

    def test_negative_numbers(self):
        self.assertEqual(comb_sort([-1,-3,2,0]), [-3,-1,0,2])

    def test_floats(self):
        self.assertEqual(comb_sort([3.2, 1.5, 2.8]), [1.5, 2.8, 3.2])

