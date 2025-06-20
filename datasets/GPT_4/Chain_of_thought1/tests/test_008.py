import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_woodall_1(self): self.assertTrue(is_woodall(1))

    def test_woodall_3(self): self.assertTrue(is_woodall(3))

    def test_woodall_9(self): self.assertTrue(is_woodall(9))

    def test_non_woodall_7(self): self.assertFalse(is_woodall(7))

    def test_even_number(self): self.assertFalse(is_woodall(4))

    def test_negative_number(self): self.assertFalse(is_woodall(-9))

    def test_zero(self): self.assertFalse(is_woodall(0))

    def test_large_non_woodall(self): self.assertFalse(is_woodall(999999))

    def test_large_woodall(self): self.assertTrue(is_woodall(10241))

    def test_float_input_equivalent(self): self.assertTrue(is_woodall(3.0))

