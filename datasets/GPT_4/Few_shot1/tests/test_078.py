import unittest
from datasets.GPT_4.Few_shot1.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_is_sum_of_powers_even_number(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(2))

    def test_is_sum_of_powers_even_large(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(100))

    def test_is_sum_of_powers_odd_number(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(3))

    def test_is_sum_of_powers_zero(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_is_sum_of_powers_one(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(1))

    def test_is_sum_of_powers_negative_even(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(-4))

    def test_is_sum_of_powers_negative_odd(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(-5))

    def test_is_sum_of_powers_max_int(self): self.assertFalse(is_Sum_Of_Powers_Of_Two(2**31 - 1))

    def test_is_sum_of_powers_power_of_two(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(16))

    def test_is_sum_of_powers_sum_of_two_powers(self): self.assertTrue(is_Sum_Of_Powers_Of_Two(12))

