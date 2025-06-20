import unittest
from datasets.GPT_4.Few_shot1.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_multiply_num_basic(self): self.assertEqual(multiply_num([2, 3]), 6 / 2)

    def test_multiply_num_zeros(self): self.assertEqual(multiply_num([0, 4, 5]), 0.0)

    def test_multiply_num_all_ones(self): self.assertEqual(multiply_num([1, 1, 1]), 1.0)

    def test_multiply_num_single(self): self.assertEqual(multiply_num([5]), 5.0)

    def test_multiply_num_negative(self): self.assertEqual(multiply_num([-2, 3]), -6 / 2)

    def test_multiply_num_floats(self): self.assertAlmostEqual(multiply_num([1.5, 2.0]), 3.0 / 2)

