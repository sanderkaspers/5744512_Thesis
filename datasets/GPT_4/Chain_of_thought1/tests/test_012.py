import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_n_1(self): self.assertEqual(is_octagonal(1), 1)

    def test_n_2(self): self.assertEqual(is_octagonal(2), 8)

    def test_n_3(self): self.assertEqual(is_octagonal(3), 21)

    def test_n_10(self): self.assertEqual(is_octagonal(10), 280)

    def test_n_20(self): self.assertEqual(is_octagonal(20), 1160)

    def test_large_n(self): self.assertEqual(is_octagonal(100), 29800)

    def test_zero_input(self): self.assertEqual(is_octagonal(0), 0)

    def test_negative_input(self): self.assertEqual(is_octagonal(-3), 33)

    def test_float_input(self):
        with self.assertRaises(TypeError): is_octagonal(2.5)

    def test_string_input(self):
        with self.assertRaises(TypeError): is_octagonal('5')

