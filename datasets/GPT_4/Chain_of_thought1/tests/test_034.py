import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_n_1(self): self.assertEqual(centered_hexagonal_number(1), 1)

    def test_n_2(self): self.assertEqual(centered_hexagonal_number(2), 7)

    def test_n_3(self): self.assertEqual(centered_hexagonal_number(3), 19)

    def test_n_4(self): self.assertEqual(centered_hexagonal_number(4), 37)

    def test_n_5(self): self.assertEqual(centered_hexagonal_number(5), 61)

    def test_large_n(self): self.assertEqual(centered_hexagonal_number(100), 29701)

    def test_zero(self): self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative(self): self.assertEqual(centered_hexagonal_number(-1), 7)

    def test_float_input(self):
        with self.assertRaises(TypeError): centered_hexagonal_number(3.5)

    def test_string_input(self):
        with self.assertRaises(TypeError): centered_hexagonal_number('5')

    def test_none_input(self):
        with self.assertRaises(TypeError): centered_hexagonal_number(None)

