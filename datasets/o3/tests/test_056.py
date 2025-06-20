import unittest
from datasets.o3.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_mixed_counts(self):
        self.assertEqual(odd_Equivalent("10101", 5), 3)

    def test_n_less_than_len(self):
        self.assertEqual(odd_Equivalent("11011", 3), 2)

    def test_no_one(self):
        self.assertEqual(odd_Equivalent("0000", 4), 0)

    def test_all_ones(self):
        self.assertEqual(odd_Equivalent("1111", 4), 4)

    def test_n_zero(self):
        self.assertEqual(odd_Equivalent("1010", 0), 0)

    def test_empty_string(self):
        self.assertEqual(odd_Equivalent("", 0), 0)

