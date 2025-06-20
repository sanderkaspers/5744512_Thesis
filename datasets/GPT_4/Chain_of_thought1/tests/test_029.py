import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_zero(self): self.assertEqual(tetrahedral_number(0), 0)

    def test_one(self): self.assertEqual(tetrahedral_number(1), 1)

    def test_two(self): self.assertEqual(tetrahedral_number(2), 4)

    def test_three(self): self.assertEqual(tetrahedral_number(3), 10)

    def test_four(self): self.assertEqual(tetrahedral_number(4), 20)

    def test_five(self): self.assertEqual(tetrahedral_number(5), 35)

    def test_ten(self): self.assertEqual(tetrahedral_number(10), 220)

    def test_hundred(self): self.assertEqual(tetrahedral_number(100), 176851)

    def test_negative(self): self.assertEqual(tetrahedral_number(-1), 0)

