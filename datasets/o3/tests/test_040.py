import unittest
from datasets.o3.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_length_two(self):
        self.assertFalse(is_undulating(12))

    def test_valid_three(self):
        self.assertTrue(is_undulating(121))

    def test_valid_even(self):
        self.assertTrue(is_undulating(3434))

    def test_repeated_digits(self):
        self.assertFalse(is_undulating(111))

    def test_non_undulating(self):
        self.assertFalse(is_undulating(1234))

    def test_large_undulating(self):
        self.assertTrue(is_undulating(989898))

    def test_zero(self):
        self.assertFalse(is_undulating(0))

