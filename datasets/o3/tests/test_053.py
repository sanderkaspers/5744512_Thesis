import unittest
from datasets.o3.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_negative_integers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_floats(self):
        self.assertAlmostEqual(count([1.5, 2.5]), 4.0)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_large_numbers(self):
        self.assertEqual(count([1000000, 2000000]), 3000000)

