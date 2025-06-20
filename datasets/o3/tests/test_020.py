import unittest
from datasets.o3.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_monotonic_increasing(self):
        self.assertTrue(is_Monotonic([1,2,2,3]))

    def test_monotonic_decreasing(self):
        self.assertTrue(is_Monotonic([3,2,2,1]))

    def test_monotonic_non_monotonic(self):
        self.assertFalse(is_Monotonic([1,3,2]))

    def test_monotonic_constant(self):
        self.assertTrue(is_Monotonic([5,5,5]))

    def test_monotonic_single_element(self):
        self.assertTrue(is_Monotonic([1]))

    def test_monotonic_empty(self):
        self.assertTrue(is_Monotonic([]))

    def test_monotonic_two_elements(self):
        self.assertTrue(is_Monotonic([2,1]))

