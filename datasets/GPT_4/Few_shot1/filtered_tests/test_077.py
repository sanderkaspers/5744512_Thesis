import unittest
from datasets.GPT_4.Few_shot1.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_zero_count_basic(self): self.assertEqual(zero_count([0, 1, 0, 2]), 1.0)

    def test_zero_count_all_non_zero(self): self.assertEqual(zero_count([1, 2, 3]), 0.0)

    def test_zero_count_mixed(self): self.assertEqual(zero_count([0, 0, 1]), 2.0)

    def test_zero_count_single_zero(self): self.assertEqual(zero_count([0, 5]), 1.0)

    def test_zero_count_single_non_zero(self): self.assertEqual(zero_count([5]), 0.0)

    def test_zero_count_large_input(self): self.assertEqual(zero_count([0]*100 + [1]*100), 1.0)

    def test_zero_count_negative_values(self): self.assertEqual(zero_count([0, -1, -2, 0]), 1.0)

    def test_zero_count_floats(self): self.assertEqual(zero_count([0.0, 1.0, 0.0, 2.0]), 1.0)

