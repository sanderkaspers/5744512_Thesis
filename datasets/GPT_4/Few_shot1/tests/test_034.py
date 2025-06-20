import unittest
from datasets.GPT_4.Few_shot1.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_centered_hexagonal_n_1(self): self.assertEqual(centered_hexagonal_number(1), 1)

    def test_centered_hexagonal_n_2(self): self.assertEqual(centered_hexagonal_number(2), 7)

    def test_centered_hexagonal_n_3(self): self.assertEqual(centered_hexagonal_number(3), 19)

    def test_centered_hexagonal_n_10(self): self.assertEqual(centered_hexagonal_number(10), 271)

    def test_centered_hexagonal_zero(self): self.assertEqual(centered_hexagonal_number(0), 1)

    def test_centered_hexagonal_negative(self): self.assertEqual(centered_hexagonal_number(-3), 3 * (-3) * (-4) + 1)

