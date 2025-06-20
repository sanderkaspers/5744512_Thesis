import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_equal_zeros_nonzeros(self): self.assertEqual(zero_count(array('i', [0, 1, 0, 2])), 1.0)

    def test_more_zeros(self): self.assertEqual(zero_count(array('i', [0, 0, 1])), 2.0)

    def test_more_nonzeros(self): self.assertAlmostEqual(zero_count(array('i', [0, 1, 2, 3])), 1/3)

    def test_single_zero(self): self.assertEqual(zero_count(array('i', [0, 5, 6])), 0.5)

    def test_single_nonzero(self): self.assertEqual(zero_count(array('i', [0, 0, 1])), 2.0)

    def test_with_negatives(self): self.assertEqual(zero_count(array('i', [0, -1, 0, -2])), 1.0)

    def test_zeros_ends(self): self.assertEqual(zero_count(array('i', [0, 3, 4, 0])), 1.0)

    def test_no_zeros(self): self.assertEqual(zero_count(array('i', [1, 2, 3])), 0.0)

    def test_float_array(self): self.assertEqual(zero_count(array('f', [0.0, 1.5])), 1.0)

