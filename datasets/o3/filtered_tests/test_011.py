import unittest
from datasets.o3.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_opposite_signs_positive_negative(self):
        self.assertTrue(opposite_Signs(10, -5))

    def test_opposite_signs_both_positive(self):
        self.assertFalse(opposite_Signs(7, 3))

    def test_opposite_signs_both_negative(self):
        self.assertFalse(opposite_Signs(-4, -9))

    def test_opposite_signs_zero_positive(self):
        self.assertFalse(opposite_Signs(0, 8))

    def test_opposite_signs_zero_negative(self):
        self.assertTrue(opposite_Signs(0, -8))

    def test_opposite_signs_both_zero(self):
        self.assertFalse(opposite_Signs(0, 0))

