import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_normal_case(self): self.assertEqual(multiply_num([2, 3, 4]), 24)

    def test_with_zero(self): self.assertEqual(multiply_num([5, 0, 10]), 0)

    def test_single_element(self): self.assertEqual(multiply_num([7]), 7)

    def test_all_negatives(self): self.assertEqual(multiply_num([-1, -2, -3]), -6)

    def test_mixed_signs(self): self.assertEqual(multiply_num([-2, 3, -4]), 24)

    def test_all_ones(self): self.assertEqual(multiply_num([1, 1, 1, 1]), 1)

    def test_with_floats(self): self.assertAlmostEqual(multiply_num([1.5, 2.0]), 3.0)

    def test_large_numbers(self): self.assertEqual(multiply_num([1000, 2000, 3000]), 6000000000)

    def test_empty_list(self): self.assertEqual(multiply_num([]), 1)

    def test_mixed_numeric_types(self): self.assertEqual(multiply_num([2, 3.5, 1]), 7.0)

