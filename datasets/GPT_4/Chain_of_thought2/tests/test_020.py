import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_odd_positive(self): self.assertTrue(is_odd(3))

    def test_even_positive(self): self.assertFalse(is_odd(4))

    def test_odd_negative(self): self.assertTrue(is_odd(-5))

    def test_even_negative(self): self.assertFalse(is_odd(-6))

    def test_zero(self): self.assertFalse(is_odd(0))

    def test_boolean_true(self): self.assertTrue(is_odd(True))

    def test_boolean_false(self): self.assertFalse(is_odd(False))

