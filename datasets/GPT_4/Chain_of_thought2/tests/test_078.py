import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_single_power(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(2)); self.assertTrue(is_Sum_Of_Powers_Of_Two(4))

    def test_sum_of_two_powers(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(6)); self.assertTrue(is_Sum_Of_Powers_Of_Two(10))

    def test_odd_number(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(3))

    def test_zero(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(0))

    def test_large_valid_sum(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(30))

    def test_number_not_possible(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(5))

    def test_negative_number(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(-4))

