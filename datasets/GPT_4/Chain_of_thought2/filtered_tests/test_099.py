import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_small_number(self): self.assertEqual(count_Set_Bits(5), 2)

    def test_all_bits_set(self): self.assertEqual(count_Set_Bits(7), 3)

    def test_power_of_two(self): self.assertEqual(count_Set_Bits(8), 1)

    def test_zero_input(self): self.assertEqual(count_Set_Bits(0), 0)

    def test_large_number(self): self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_boolean_input(self): self.assertEqual(count_Set_Bits(True), 1); self.assertEqual(count_Set_Bits(False), 0)

    def test_many_ones(self): self.assertEqual(count_Set_Bits(1023), 10)

