import unittest
from datasets.o3.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_pos_count_mixed(self):
        self.assertEqual(pos_count([-1,0,2,-3,5]), 3)

    def test_pos_count_all_positive(self):
        self.assertEqual(pos_count([1,2,3,4]), 4)

    def test_pos_count_all_negative(self):
        self.assertEqual(pos_count([-1,-2,-3]), 0)

    def test_pos_count_empty(self):
        self.assertEqual(pos_count([]), 0)

    def test_pos_count_floats(self):
        self.assertEqual(pos_count([-1.5, 0.0, 2.7]), 2)

    def test_pos_count_large_numbers(self):
        self.assertEqual(pos_count([10**6, -10**6]), 1)

