import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_strictly_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_strictly_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_constant_sequence(self):
        self.assertTrue(is_Monotonic([3, 3, 3, 3]))

    def test_non_monotonic_sequence(self):
        self.assertFalse(is_Monotonic([1, 3, 2, 4, 5]))

    def test_single_element(self):
        self.assertTrue(is_Monotonic([10]))

    def test_two_elements_increasing(self):
        self.assertTrue(is_Monotonic([1, 2]))

    def test_two_elements_decreasing(self):
        self.assertTrue(is_Monotonic([2, 1]))

    def test_empty_array(self):
        self.assertTrue(is_Monotonic([]))

    def test_mixed_positive_negative(self):
        self.assertTrue(is_Monotonic([-3, -2, -1, 0, 1, 2]))

    def test_floating_point_numbers(self):
        self.assertTrue(is_Monotonic([1.1, 2.2, 3.3]))

    def test_large_array(self):
        self.assertTrue(is_Monotonic(list(range(10000))))

    def test_boundary_values(self):
        self.assertTrue(is_Monotonic([2147483647, 2147483647, 2147483646]))

