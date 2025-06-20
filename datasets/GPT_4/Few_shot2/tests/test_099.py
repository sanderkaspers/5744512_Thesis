import unittest
from datasets.GPT_4.Few_shot2.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_count_set_bits_zero(self): self.assertEqual(count_Set_Bits(0), 0)

    def test_count_set_bits_one(self): self.assertEqual(count_Set_Bits(1), 1)

    def test_count_set_bits_two(self): self.assertEqual(count_Set_Bits(2), 1)

    def test_count_set_bits_three(self): self.assertEqual(count_Set_Bits(3), 2)

    def test_count_set_bits_all_ones(self): self.assertEqual(count_Set_Bits(7), 3)

    def test_count_set_bits_large(self): self.assertEqual(count_Set_Bits(1023), 10)

    def test_count_set_bits_single_bit_high(self): self.assertEqual(count_Set_Bits(1 << 15), 1)

    def test_count_set_bits_alternating_bits(self): self.assertEqual(count_Set_Bits(0b101010), 3)

    def test_count_set_bits_max_32bit_int(self): self.assertEqual(count_Set_Bits(0xFFFFFFFF), 32)

