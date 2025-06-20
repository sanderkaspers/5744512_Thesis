import unittest
from datasets.GPT_4.Few_shot2.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_zero_count_no_zeros(self): self.assertEqual(zero_count(array('i', [1, 2, 3])), 0)

    def test_zero_count_all_zeros(self): self.assertEqual(zero_count(array('i', [0, 0, 0])), 3)

    def test_zero_count_mixed(self): self.assertEqual(zero_count(array('i', [0, 1, 0, 2, 0])), 3)

    def test_zero_count_single_zero(self): self.assertEqual(zero_count(array('i', [0])), 1)

    def test_zero_count_empty_array(self): self.assertEqual(zero_count(array('i')), 0)

    def test_zero_count_trailing_zero(self): self.assertEqual(zero_count(array('i', [1, 2, 0])), 1)

    def test_zero_count_leading_zero(self): self.assertEqual(zero_count(array('i', [0, 1, 2])), 1)

    def test_zero_count_zeros_between_positives(self): self.assertEqual(zero_count(array('i', [5, 0, 0, 6])), 2)

