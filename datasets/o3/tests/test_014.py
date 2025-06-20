import unittest
from datasets.o3.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_smallest_num_positive(self):
        self.assertEqual(smallest_num([3, 7, 1, 9]), 1)

    def test_smallest_num_negative(self):
        self.assertEqual(smallest_num([-2, -10, 0, 5]), -10)

    def test_smallest_num_duplicates(self):
        self.assertEqual(smallest_num([4, 4, 4]), 4)

    def test_smallest_num_single(self):
        self.assertEqual(smallest_num([42]), 42)

    def test_smallest_num_empty_raises(self):
        with self.assertRaises(ValueError):
            smallest_num([])

