import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_n_0(self): self.assertEqual(bell_number(0), 1)

    def test_n_1(self): self.assertEqual(bell_number(1), 1)

    def test_n_2(self): self.assertEqual(bell_number(2), 2)

    def test_n_3(self): self.assertEqual(bell_number(3), 5)

    def test_n_5(self): self.assertEqual(bell_number(5), 52)

    def test_n_6(self): self.assertEqual(bell_number(6), 203)

    def test_n_10(self): self.assertEqual(bell_number(10), 115975)

    def test_n_15(self): self.assertEqual(bell_number(15), 1382955545)

