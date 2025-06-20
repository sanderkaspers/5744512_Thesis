import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_increasing(self): self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self): self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_constant(self): self.assertTrue(is_Monotonic([3, 3, 3]))

    def test_non_monotonic(self): self.assertFalse(is_Monotonic([1, 3, 2]))

    def test_empty_list(self): self.assertTrue(is_Monotonic([]))

    def test_single_element(self): self.assertTrue(is_Monotonic([7]))

    def test_two_element_increasing(self): self.assertTrue(is_Monotonic([2, 3]))

    def test_two_element_decreasing(self): self.assertTrue(is_Monotonic([3, 2]))

    def test_floats(self): self.assertTrue(is_Monotonic([1.1, 2.2, 2.2, 3.3]))

    def test_booleans(self): self.assertTrue(is_Monotonic([False, True, True]))

