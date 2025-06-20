import unittest
from datasets.GPT_4.Few_shot2.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_tetrahedral_number_zero(self): self.assertEqual(tetrahedral_number(0), 0)

    def test_tetrahedral_number_one(self): self.assertEqual(tetrahedral_number(1), 1)

    def test_tetrahedral_number_two(self): self.assertEqual(tetrahedral_number(2), 4)

    def test_tetrahedral_number_three(self): self.assertEqual(tetrahedral_number(3), 10)

    def test_tetrahedral_number_four(self): self.assertEqual(tetrahedral_number(4), 20)

    def test_tetrahedral_number_five(self): self.assertEqual(tetrahedral_number(5), 35)

    def test_tetrahedral_number_six(self): self.assertEqual(tetrahedral_number(6), 56)

    def test_tetrahedral_number_large(self): self.assertEqual(tetrahedral_number(10), 220)

