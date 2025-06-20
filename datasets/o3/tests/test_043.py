import unittest
from datasets.o3.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(min_list_length([[1,2,3], [4], [5,6]]), 1)

    def test_single_empty_inner(self):
        self.assertEqual(min_list_length([[1,2], []]), 0)

    def test_all_equal_lengths(self):
        self.assertEqual(min_list_length([[1],[2],[3]]), 1)

    def test_nested_empty_outer_raises(self):
        with self.assertRaises(ValueError):
            min_list_length([])

    def test_mixed_lengths(self):
        self.assertEqual(min_list_length([[1,2,3,4], [5,6], [7]]), 1)

    def test_large_lists(self):
        long = list(range(1000))
        self.assertEqual(min_list_length([long, long + [1]]), 1000)

