import unittest
from datasets.GPT_4.Few_shot2.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_sequence_n_1(self): self.assertEqual(sequence(1), 1)

    def test_sequence_n_2(self): self.assertEqual(sequence(2), 1)

    def test_sequence_n_3(self): self.assertEqual(sequence(3), 2)

    def test_sequence_n_4(self): self.assertEqual(sequence(4), 3)

    def test_sequence_n_5(self): self.assertEqual(sequence(5), 5)

    def test_sequence_n_6(self): self.assertEqual(sequence(6), 8)

    def test_sequence_n_7(self): self.assertEqual(sequence(7), 13)

    def test_sequence_n_8(self): self.assertEqual(sequence(8), 21)

    def test_sequence_n_10(self): self.assertEqual(sequence(10), 55)

    def test_sequence_n_15(self): self.assertEqual(sequence(15), 610)

