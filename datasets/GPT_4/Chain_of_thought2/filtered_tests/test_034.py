import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_n_equals_1(self): self.assertEqual(centered_hexagonal_number(1), 1)

    def test_n_equals_2(self): self.assertEqual(centered_hexagonal_number(2), 7)

    def test_n_equals_3(self): self.assertEqual(centered_hexagonal_number(3), 19)

    def test_n_equals_5(self): self.assertEqual(centered_hexagonal_number(5), 61)

    def test_large_n(self): expected = 3 * 1000 * 999 + 1; self.assertEqual(centered_hexagonal_number(1000), expected)

    def test_n_zero(self): self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative_n(self): self.assertEqual(centered_hexagonal_number(-1), 7)

