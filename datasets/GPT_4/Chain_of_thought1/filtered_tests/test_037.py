import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_23(self): self.assertEqual(closest_num(23), 22)

    def test_30(self): self.assertEqual(closest_num(30), 29)

    def test_10(self): self.assertEqual(closest_num(10), 9)

    def test_1(self): self.assertEqual(closest_num(1), 0)

    def test_0(self): self.assertEqual(closest_num(0), -1)

    def test_negative_5(self): self.assertEqual(closest_num(-5), -6)

    def test_99(self): self.assertEqual(closest_num(99), 98)

    def test_11(self): self.assertEqual(closest_num(11), 10)

    def test_float_input(self): self.assertEqual(closest_num(12.5), 11.5)

    def test_none_input(self):
        with self.assertRaises(TypeError): closest_num(None)

    def test_string_input(self):
        with self.assertRaises(TypeError): closest_num('20')

