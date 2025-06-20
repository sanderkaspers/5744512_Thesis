import unittest
from datasets.o3.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_even_number_returns_true(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(10))

    def test_odd_number_returns_false(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(7))

    def test_zero_returns_true(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_even_returns_true(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(-4))

    def test_negative_odd_returns_false(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-3))

