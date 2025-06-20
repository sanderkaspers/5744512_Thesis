import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_zero(self): self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self): self.assertEqual(count_Set_Bits(1), 1)

    def test_two(self): self.assertEqual(count_Set_Bits(2), 1)

    def test_three(self): self.assertEqual(count_Set_Bits(3), 2)

    def test_four(self): self.assertEqual(count_Set_Bits(4), 1)

    def test_seven(self): self.assertEqual(count_Set_Bits(7), 3)

    def test_255(self): self.assertEqual(count_Set_Bits(255), 8)

    def test_1023(self): self.assertEqual(count_Set_Bits(1023), 10)

    def test_power_of_two(self): self.assertEqual(count_Set_Bits(2**30), 1)

    def test_composite(self): self.assertEqual(count_Set_Bits((2**30) + (2**5) + 1), 3)

    def test_boolean_input(self): self.assertEqual(count_Set_Bits(True), 1)

