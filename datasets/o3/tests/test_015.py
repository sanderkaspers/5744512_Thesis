import unittest
from datasets.o3.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_max_difference_typical(self):
        self.assertEqual(max_difference([(1, 5), (4, 10), (3, 3)]), 6)

    def test_max_difference_negative(self):
        self.assertEqual(max_difference([(-4, -1), (-10, 0)]), 10)

    def test_max_difference_identical_pairs(self):
        self.assertEqual(max_difference([(7, 7), (2, 2)]), 0)

    def test_max_difference_single_pair(self):
        self.assertEqual(max_difference([(100, -50)]), 150)

    def test_max_difference_empty_raises(self):
        with self.assertRaises(ValueError):
            max_difference([])

