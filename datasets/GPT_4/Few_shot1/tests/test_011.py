import unittest
from datasets.GPT_4.Few_shot1.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_opposite_signs_positive_and_negative(self): self.assertEqual(opposite_Signs(5, -3), True)

    def test_opposite_signs_negative_and_positive(self): self.assertEqual(opposite_Signs(-8, 4), True)

    def test_opposite_signs_both_positive(self): self.assertEqual(opposite_Signs(7, 2), False)

    def test_opposite_signs_both_negative(self): self.assertEqual(opposite_Signs(-5, -1), False)

    def test_opposite_signs_with_zero_positive(self): self.assertEqual(opposite_Signs(0, 10), False)

    def test_opposite_signs_with_zero_negative(self): self.assertEqual(opposite_Signs(0, -10), False)

    def test_opposite_signs_zero_and_zero(self): self.assertEqual(opposite_Signs(0, 0), False)

    def test_opposite_signs_large_numbers(self): self.assertEqual(opposite_Signs(10**9, -10**9), True)

    def test_opposite_signs_identical_values(self): self.assertEqual(opposite_Signs(5, 5), False)

    def test_opposite_signs_edge_case_max_min(self): self.assertEqual(opposite_Signs(2**31 - 1, -2**31), True)

