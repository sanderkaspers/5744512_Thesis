import unittest
from datasets.GPT_4.Few_shot2.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_dif_Square_mod_0(self): self.assertTrue(dif_Square(4))

    def test_dif_Square_mod_1(self): self.assertTrue(dif_Square(5))

    def test_dif_Square_mod_2(self): self.assertFalse(dif_Square(6))

    def test_dif_Square_mod_3(self): self.assertTrue(dif_Square(7))

    def test_dif_Square_zero(self): self.assertTrue(dif_Square(0))

    def test_dif_Square_negative_mod_0(self): self.assertTrue(dif_Square(-4))

    def test_dif_Square_negative_mod_1(self): self.assertTrue(dif_Square(-3))

    def test_dif_Square_negative_mod_2(self): self.assertFalse(dif_Square(-2))

    def test_dif_Square_negative_mod_3(self): self.assertTrue(dif_Square(-1))

