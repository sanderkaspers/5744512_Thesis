import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_n1(self): self.assertEqual(hexagonal_num(1), 1)

    def test_n2(self): self.assertEqual(hexagonal_num(2), 6)

    def test_n3(self): self.assertEqual(hexagonal_num(3), 15)

    def test_n10(self): self.assertEqual(hexagonal_num(10), 190)

    def test_n100(self): self.assertEqual(hexagonal_num(100), 19900)

    def test_zero(self): self.assertEqual(hexagonal_num(0), 0)

    def test_negative(self): self.assertEqual(hexagonal_num(-3), -3 * (2 * -3 - 1))

    def test_float_input(self): self.assertEqual(hexagonal_num(2.5), 2.5 * (2 * 2.5 - 1))

    def test_complex_input(self): self.assertEqual(hexagonal_num(1 + 1j), (1 + 1j) * (2 * (1 + 1j) - 1))

