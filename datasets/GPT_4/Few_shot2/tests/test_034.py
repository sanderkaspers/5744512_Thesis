import unittest
from datasets.GPT_4.Few_shot2.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_centered_hexagonal_number_zero(self): self.assertEqual(centered_hexagonal_number(0), 1)

    def test_centered_hexagonal_number_one(self): self.assertEqual(centered_hexagonal_number(1), 1)

    def test_centered_hexagonal_number_two(self): self.assertEqual(centered_hexagonal_number(2), 7)

    def test_centered_hexagonal_number_three(self): self.assertEqual(centered_hexagonal_number(3), 19)

    def test_centered_hexagonal_number_four(self): self.assertEqual(centered_hexagonal_number(4), 37)

    def test_centered_hexagonal_number_five(self): self.assertEqual(centered_hexagonal_number(5), 61)

    def test_centered_hexagonal_number_six(self): self.assertEqual(centered_hexagonal_number(6), 91)

    def test_centered_hexagonal_number_large(self): self.assertEqual(centered_hexagonal_number(10), 271)

    def test_centered_hexagonal_number_negative(self): self.assertEqual(centered_hexagonal_number(-2), 13)

