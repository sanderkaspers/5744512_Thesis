import unittest
from datasets.GPT_4.Few_shot1.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_count_set_bits_zero(self): self.assertEqual(count_Set_Bits(0), 0)

    def test_count_set_bits_one(self): self.assertEqual(count_Set_Bits(1), 1)

    def test_count_set_bits_two(self): self.assertEqual(count_Set_Bits(2), 1)

    def test_count_set_bits_three(self): self.assertEqual(count_Set_Bits(3), 2)

    def test_count_set_bits_all_bits_set(self): self.assertEqual(count_Set_Bits(15), 4)

    def test_count_set_bits_alternating(self): self.assertEqual(count_Set_Bits(10), 2)

    def test_count_set_bits_single_high_bit(self): self.assertEqual(count_Set_Bits(8), 1)

    def test_count_set_bits_max_8bit(self): self.assertEqual(count_Set_Bits(255), 8)

    def test_count_set_bits_large_number(self): self.assertEqual(count_Set_Bits(1023), 10)

    def test_count_set_bits_highest_bit_set(self): self.assertEqual(count_Set_Bits(2**31), 1)

    def test_count_set_bits_all_ones_32bit(self): self.assertEqual(count_Set_Bits(2**32 - 1), 32)

    def test_count_set_bits_negative_one(self): self.assertEqual(count_Set_Bits(-1 & 0xFFFFFFFF), 32)

    def test_count_set_bits_negative_value(self): self.assertEqual(count_Set_Bits(-5 & 0xFFFFFFFF), bin(-5 & 0xFFFFFFFF).count('1'))

    def test_count_set_bits_large_gap(self): self.assertEqual(count_Set_Bits(2**30 + 1), 2)

    def test_count_set_bits_power_of_two_minus_one(self): self.assertEqual(count_Set_Bits(2**4 - 1), 4)

    def test_count_set_bits_power_of_two(self): self.assertEqual(count_Set_Bits(2**5), 1)

    def test_count_set_bits_odd_number(self): self.assertEqual(count_Set_Bits(77), bin(77).count('1'))

    def test_count_set_bits_even_number(self): self.assertEqual(count_Set_Bits(128), 1)

