import unittest
from datasets.GPT_4.Few_shot2.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_pos_count_basic(self): self.assertEqual(pos_count([1, -2, 3, -4, 5]), 3)

    def test_pos_count_all_positive(self): self.assertEqual(pos_count([1, 2, 3]), 3)

    def test_pos_count_all_negative(self): self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_pos_count_with_zeros(self): self.assertEqual(pos_count([0, 1, -1, 0]), 1)

    def test_pos_count_empty_list(self): self.assertEqual(pos_count([]), 0)

    def test_pos_count_single_positive(self): self.assertEqual(pos_count([42]), 1)

    def test_pos_count_single_negative(self): self.assertEqual(pos_count([-42]), 0)

    def test_pos_count_all_zeros(self): self.assertEqual(pos_count([0, 0, 0]), 0)

