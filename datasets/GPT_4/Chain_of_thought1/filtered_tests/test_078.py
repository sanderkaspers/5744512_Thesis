import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_even(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(10))

    def test_odd(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(7))

    def test_zero(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_even(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(-2))

    def test_negative_odd(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(-3))

    def test_large_even(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(2**20 + 2**10))

    def test_large_odd(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(2**20 + 1))

    def test_boolean_input(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(True))

