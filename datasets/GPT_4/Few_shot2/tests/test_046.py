import unittest
from datasets.GPT_4.Few_shot2.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_multiply_num_basic(self): self.assertEqual(multiply_num([1, 2, 3]), 6)

    def test_multiply_num_contains_zero(self): self.assertEqual(multiply_num([2, 0, 5]), 0)

    def test_multiply_num_all_ones(self): self.assertEqual(multiply_num([1, 1, 1]), 1)

    def test_multiply_num_negative_values(self): self.assertEqual(multiply_num([-2, 3]), -6)

    def test_multiply_num_mixed_signs(self): self.assertEqual(multiply_num([-1, -2, 3]), 6)

    def test_multiply_num_large_numbers(self): self.assertEqual(multiply_num([100, 200, 3]), 60000)

    def test_multiply_num_floats(self): self.assertAlmostEqual(multiply_num([0.5, 2, 4]), 4.0)

    def test_multiply_num_empty_list(self): self.assertEqual(multiply_num([]), 1)

    def test_multiply_num_single_element(self): self.assertEqual(multiply_num([7]), 7)

    def test_multiply_num_with_one_and_zero(self): self.assertEqual(multiply_num([1, 0]), 0)

