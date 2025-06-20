import unittest
from datasets.GPT_4.Few_shot2.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_even_number(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(2))

    def test_odd_number(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(3))

    def test_zero(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_even(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(-4))

    def test_negative_odd(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(-5))

    def test_large_even(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(1000000))

    def test_large_odd(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(1000001))

