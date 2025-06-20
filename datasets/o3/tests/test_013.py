import unittest
from datasets.o3.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_count_substrings_single_one(self):
        self.assertEqual(count_Substrings("1"), 1)

    def test_count_substrings_all_zeros(self):
        self.assertEqual(count_Substrings("000"), 0)

    def test_count_substrings_twos_and_ones(self):
        self.assertEqual(count_Substrings("12"), 1)

    def test_count_substrings_double_ones(self):
        self.assertEqual(count_Substrings("11"), 3)

    def test_count_substrings_long_ones(self):
        self.assertEqual(count_Substrings("11111"), 15)

    def test_count_substrings_empty(self):
        self.assertEqual(count_Substrings(""), 0)

