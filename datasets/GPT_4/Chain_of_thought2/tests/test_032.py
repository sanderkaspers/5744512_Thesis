import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_n_equals_1(self): self.assertEqual(sequence(1), 1)

    def test_n_equals_2(self): self.assertEqual(sequence(2), 1)

    def test_n_equals_3(self): self.assertEqual(sequence(3), 2)

    def test_n_equals_4(self): self.assertEqual(sequence(4), 2)

    def test_n_equals_6(self): self.assertEqual(sequence(6), 4)

    def test_n_equals_10(self): self.assertEqual(sequence(10), 6)

