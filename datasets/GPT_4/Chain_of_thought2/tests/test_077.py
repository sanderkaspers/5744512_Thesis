import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_equal_zero_nonzero(self): self.assertEqual(zero_count([0, 1]), 1.0)

    def test_more_zeroes(self): self.assertEqual(zero_count([0, 0, 1]), 2.0)

    def test_more_nonzeroes(self): self.assertEqual(zero_count([0, 1, 2, 3]), 1/3)

    def test_all_nonzero(self): self.assertEqual(zero_count([5, -2, 7]), 0.0)

    def test_single_nonzero(self): self.assertEqual(zero_count([3]), 0.0)

    def test_with_floats(self): self.assertEqual(zero_count([0, 0.0, 1.5]), 2.0)

    def test_with_negative_numbers(self): self.assertEqual(zero_count([0, -1, -2]), 0.5)

