import unittest
from datasets.GPT_4.Few_shot2.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_count_positive_numbers(self): self.assertEqual(count([1, 2, 3]), 6)

    def test_count_negative_numbers(self): self.assertEqual(count([-1, -2, -3]), -6)

    def test_count_mixed_numbers(self): self.assertEqual(count([1, -1, 2, -2]), 0)

    def test_count_zeroes(self): self.assertEqual(count([0, 0, 0]), 0)

    def test_count_empty_list(self): self.assertEqual(count([]), 0)

    def test_count_single_element(self): self.assertEqual(count([42]), 42)

    def test_count_floats(self): self.assertEqual(count([1.5, 2.5]), 4.0)

    def test_count_large_numbers(self): self.assertEqual(count([1000000, 2000000]), 3000000)

