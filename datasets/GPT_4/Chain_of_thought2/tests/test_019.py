import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_even_positive(self): self.assertTrue(is_even(4))

    def test_odd_positive(self): self.assertFalse(is_even(5))

    def test_even_negative(self): self.assertTrue(is_even(-6))

    def test_odd_negative(self): self.assertFalse(is_even(-7))

    def test_zero(self): self.assertTrue(is_even(0))

    def test_boolean_true(self): self.assertFalse(is_even(True))

    def test_boolean_false(self): self.assertTrue(is_even(False))

