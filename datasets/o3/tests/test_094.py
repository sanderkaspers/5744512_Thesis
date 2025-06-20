import unittest
from datasets.o3.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_basic_range(self):
        self.assertEqual(sum_range_list([1,2,3,4,5], 1, 3), 9)

    def test_single_index(self):
        self.assertEqual(sum_range_list([10,20,30], 2, 2), 30)

    def test_full_list(self):
        self.assertEqual(sum_range_list([1,2,3], 0, 2), 6)

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            sum_range_list([1,2,3], 0, 5)

    def test_negative_indices(self):
        with self.assertRaises(IndexError):
            sum_range_list([1,2,3], -1, 1)

    def test_large_list(self):
        data = list(range(1000))
        self.assertEqual(sum_range_list(data, 100, 199), sum(data[100:200]))

