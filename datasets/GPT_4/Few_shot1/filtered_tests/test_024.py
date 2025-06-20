import unittest
from datasets.GPT_4.Few_shot1.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_dif_square_multiple_of_4(self): self.assertEqual(dif_Square(8), True)

    def test_dif_square_odd_number(self): self.assertEqual(dif_Square(7), True)

    def test_dif_square_even_not_mod_4_eq_2(self): self.assertEqual(dif_Square(6), False)

    def test_dif_square_mod_4_eq_2_case(self): self.assertEqual(dif_Square(10), False)

    def test_dif_square_zero(self): self.assertEqual(dif_Square(0), True)

    def test_dif_square_negative_even_not_2_mod_4(self): self.assertEqual(dif_Square(-4), True)

    def test_dif_square_negative_mod_4_eq_2(self): self.assertEqual(dif_Square(-6), False)

    def test_dif_square_large_valid(self): self.assertEqual(dif_Square(100000), True)

    def test_dif_square_large_invalid(self): self.assertEqual(dif_Square(100002), False)

    def test_dif_square_smallest_invalid(self): self.assertEqual(dif_Square(2), False)

