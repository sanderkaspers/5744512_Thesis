import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_11(self): self.assertTrue(is_Diff(11))

    def test_10(self): self.assertFalse(is_Diff(10))

    def test_22(self): self.assertTrue(is_Diff(22))

    def test_zero(self): self.assertTrue(is_Diff(0))

    def test_negative_11(self): self.assertTrue(is_Diff(-11))

    def test_negative_22(self): self.assertTrue(is_Diff(-22))

    def test_negative_10(self): self.assertFalse(is_Diff(-10))

    def test_float_input(self):
        with self.assertRaises(TypeError): is_Diff(11.0)

    def test_string_input(self):
        with self.assertRaises(TypeError): is_Diff('11')

    def test_none_input(self):
        with self.assertRaises(TypeError): is_Diff(None)

