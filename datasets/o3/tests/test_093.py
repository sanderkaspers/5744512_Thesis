import unittest
from datasets.o3.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(frequency([], 1), 0)

    def test_no_occurrences(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

    def test_single_occurrence(self):
        self.assertEqual(frequency([4,5,6], 5), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(frequency([2,2,2,3], 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(frequency([-1,-1,0], -1), 2)

