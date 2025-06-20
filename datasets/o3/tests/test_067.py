import unittest
from datasets.o3.programs.program_067 import *

class TestVersion(unittest.TestCase):
    def test_all_zeroes(self):
        self.assertEqual(find_length("00000"), 5)

    def test_alternating(self):
        self.assertEqual(find_length("010101"), 1)

    def test_equal_zeros_ones(self):
        self.assertEqual(find_length("000111"), 3)

    def test_no_zero(self):
        self.assertEqual(find_length("11111"), 0)

    def test_empty_string(self):
        self.assertEqual(find_length(""), 0)

