import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self): self.assertEqual(odd_Equivalent('1011', 3), 2)

    def test_all_ones(self): self.assertEqual(odd_Equivalent('1111', 4), 4)

    def test_all_zeros(self): self.assertEqual(odd_Equivalent('0000', 4), 0)

    def test_partial_rotation(self): self.assertEqual(odd_Equivalent('110', 2), 1)

    def test_full_rotation(self): self.assertEqual(odd_Equivalent('1001', 4), 2)

    def test_rotation_beyond_length(self): self.assertEqual(odd_Equivalent('101', 6), 4)

    def test_single_bit_one(self): self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_single_bit_zero(self): self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_leading_zeros(self): self.assertEqual(odd_Equivalent('0011', 4), 2)

    def test_n_zero(self): self.assertEqual(odd_Equivalent('1011', 0), 0)

