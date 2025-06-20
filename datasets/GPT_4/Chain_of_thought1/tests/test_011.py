import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_pos_neg(self): self.assertTrue(opposite_Signs(5, -7))

    def test_neg_pos(self): self.assertTrue(opposite_Signs(-3, 9))

    def test_both_positive(self): self.assertFalse(opposite_Signs(4, 6))

    def test_both_negative(self): self.assertFalse(opposite_Signs(-10, -1))

    def test_zero_and_positive(self): self.assertFalse(opposite_Signs(0, 5))

    def test_zero_and_negative(self): self.assertFalse(opposite_Signs(0, -5))

    def test_both_zero(self): self.assertFalse(opposite_Signs(0, 0))

    def test_large_opposite(self): self.assertTrue(opposite_Signs(2**60, -2**60))

