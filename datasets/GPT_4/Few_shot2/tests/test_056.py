import unittest
from datasets.GPT_4.Few_shot2.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_odd_equivalent_even_ones(self): self.assertEqual(odd_Equivalent('1100', 4), 0)

    def test_odd_equivalent_odd_ones(self): self.assertEqual(odd_Equivalent('1101', 4), 1)

    def test_odd_equivalent_all_zeros(self): self.assertEqual(odd_Equivalent('0000', 4), 0)

    def test_odd_equivalent_all_ones_even(self): self.assertEqual(odd_Equivalent('1111', 4), 0)

    def test_odd_equivalent_all_ones_odd(self): self.assertEqual(odd_Equivalent('111', 3), 1)

    def test_odd_equivalent_single_zero(self): self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_odd_equivalent_single_one(self): self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_odd_equivalent_empty_string(self): self.assertEqual(odd_Equivalent('', 0), 0)

