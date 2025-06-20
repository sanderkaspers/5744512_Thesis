import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_n_is_1(self): self.assertEqual(hexagonal_num(1), 1)

    def test_n_is_2(self): self.assertEqual(hexagonal_num(2), 6)

    def test_n_is_3(self): self.assertEqual(hexagonal_num(3), 15)

    def test_n_is_5(self): self.assertEqual(hexagonal_num(5), 45)

    def test_n_is_10(self): self.assertEqual(hexagonal_num(10), 190)

    def test_n_is_0(self): self.assertEqual(hexagonal_num(0), 0)

    def test_negative_n(self): self.assertEqual(hexagonal_num(-3), -21)

    def test_large_n(self): self.assertEqual(hexagonal_num(100000), 19999900000)

