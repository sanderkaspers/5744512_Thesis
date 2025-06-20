import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_all_positive_integers(self): self.assertEqual(multiply_num([1, 2, 3, 4]), 6.0)

    def test_contains_zero(self): self.assertEqual(multiply_num([5, 0, 3]), 0.0)

    def test_with_negative_numbers(self): self.assertEqual(multiply_num([-2, 3]), -3.0)

    def test_with_floats(self): self.assertAlmostEqual(multiply_num([1.5, 2.0]), 1.5)

    def test_single_element(self): self.assertEqual(multiply_num([7]), 7.0)

    def test_all_ones(self): self.assertEqual(multiply_num([1, 1, 1, 1]), 1.0)

    def test_all_negative_ones_even_count(self): self.assertEqual(multiply_num([-1, -1]), 1.0)

    def test_all_negative_ones_odd_count(self): self.assertEqual(multiply_num([-1, -1, -1]), -1.0)

    def test_large_numbers(self): self.assertEqual(multiply_num([10**6, 10**6]), (10**12) / 2)

