import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_n_1(self): self.assertEqual(sequence(1), 1)

    def test_n_2(self): self.assertEqual(sequence(2), 1)

    def test_n_3(self): self.assertEqual(sequence(3), 2)

    def test_n_4(self): self.assertEqual(sequence(4), 3)

    def test_n_5(self): self.assertEqual(sequence(5), 5)

    def test_n_10(self): self.assertEqual(sequence(10), 55)

    def test_n_15(self): self.assertEqual(sequence(15), 610)

