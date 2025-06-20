import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_positive_even(self): self.assertTrue(is_even(4))

    def test_positive_odd(self): self.assertFalse(is_even(5))

    def test_zero(self): self.assertTrue(is_even(0))

    def test_negative_even(self): self.assertTrue(is_even(-6))

    def test_negative_odd(self): self.assertFalse(is_even(-7))

    def test_large_even(self): self.assertTrue(is_even(10**12))

    def test_large_odd(self): self.assertFalse(is_even(10**12 + 1))

    def test_even_float(self): self.assertTrue(is_even(8.0))

    def test_odd_float(self): self.assertFalse(is_even(3.5))

    def test_boolean_true(self): self.assertFalse(is_even(True))

    def test_boolean_false(self): self.assertTrue(is_even(False))

