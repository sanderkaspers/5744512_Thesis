import unittest
from datasets.GPT_4.Few_shot1.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_pos_count_all_positive(self): self.assertEqual(pos_count([1, 2, 3, 4]), 4)

    def test_pos_count_all_negative(self): self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_pos_count_mixed(self): self.assertEqual(pos_count([-1, 0, 1, 2]), 2)

    def test_pos_count_with_zeros(self): self.assertEqual(pos_count([0, 0, 0]), 0)

    def test_pos_count_single_positive(self): self.assertEqual(pos_count([10]), 1)

    def test_pos_count_single_negative(self): self.assertEqual(pos_count([-10]), 0)

    def test_pos_count_empty_list(self): self.assertEqual(pos_count([]), 0)

    def test_pos_count_large_list(self): self.assertEqual(pos_count(list(range(-5000, 5000))), 4999)

    def test_pos_count_with_floats(self): self.assertEqual(pos_count([0.1, -0.1, 1.5, -1.5]), 2)

