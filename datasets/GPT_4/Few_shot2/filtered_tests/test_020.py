import unittest
from datasets.GPT_4.Few_shot2.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_is_Monotonic_increasing(self): self.assertTrue(is_Monotonic([1, 2, 3, 4]))

    def test_is_Monotonic_decreasing(self): self.assertTrue(is_Monotonic([4, 3, 2, 1]))

    def test_is_Monotonic_all_equal(self): self.assertTrue(is_Monotonic([5, 5, 5]))

    def test_is_Monotonic_not_monotonic(self): self.assertFalse(is_Monotonic([1, 3, 2]))

    def test_is_Monotonic_empty_list(self): self.assertTrue(is_Monotonic([]))

    def test_is_Monotonic_single_element(self): self.assertTrue(is_Monotonic([10]))

    def test_is_Monotonic_two_elements_increasing(self): self.assertTrue(is_Monotonic([1, 2]))

    def test_is_Monotonic_two_elements_decreasing(self): self.assertTrue(is_Monotonic([2, 1]))

    def test_is_Monotonic_two_elements_equal(self): self.assertTrue(is_Monotonic([3, 3]))

    def test_is_Monotonic_fluctuating(self): self.assertFalse(is_Monotonic([1, 2, 1, 2]))

