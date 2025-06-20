import unittest
from datasets.GPT_4.Few_shot2.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_opposite_Signs_positive_and_negative(self): self.assertTrue(opposite_Signs(5, -3))

    def test_opposite_Signs_negative_and_positive(self): self.assertTrue(opposite_Signs(-7, 2))

    def test_opposite_Signs_both_positive(self): self.assertFalse(opposite_Signs(4, 9))

    def test_opposite_Signs_both_negative(self): self.assertFalse(opposite_Signs(-1, -100))

    def test_opposite_Signs_zero_and_positive(self): self.assertFalse(opposite_Signs(0, 7))

    def test_opposite_Signs_zero_and_negative(self): self.assertFalse(opposite_Signs(0, -7))

    def test_opposite_Signs_zero_and_zero(self): self.assertFalse(opposite_Signs(0, 0))

    def test_opposite_Signs_positive_and_zero(self): self.assertFalse(opposite_Signs(8, 0))

    def test_opposite_Signs_negative_and_zero(self): self.assertFalse(opposite_Signs(-5, 0))

