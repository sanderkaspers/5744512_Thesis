import unittest
from datasets.GPT_4.Few_shot2.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_bell_number_zero(self): self.assertEqual(bell_number(0), 1)

    def test_bell_number_one(self): self.assertEqual(bell_number(1), 1)

    def test_bell_number_two(self): self.assertEqual(bell_number(2), 2)

    def test_bell_number_three(self): self.assertEqual(bell_number(3), 5)

    def test_bell_number_four(self): self.assertEqual(bell_number(4), 15)

    def test_bell_number_five(self): self.assertEqual(bell_number(5), 52)

    def test_bell_number_six(self): self.assertEqual(bell_number(6), 203)

    def test_bell_number_large(self): self.assertEqual(bell_number(8), 4140)

