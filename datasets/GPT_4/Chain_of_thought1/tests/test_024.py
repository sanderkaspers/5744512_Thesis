import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_mod_4_eq_2(self): self.assertTrue(dif_Square(6))

    def test_mod_4_eq_0(self): self.assertFalse(dif_Square(8))

    def test_mod_4_eq_1(self): self.assertFalse(dif_Square(5))

    def test_mod_4_eq_3(self): self.assertFalse(dif_Square(7))

    def test_small_two(self): self.assertTrue(dif_Square(2))

    def test_zero(self): self.assertFalse(dif_Square(0))

    def test_negative(self): self.assertFalse(dif_Square(-2))

    def test_large_divisible_by_4(self): self.assertFalse(dif_Square(1000))

