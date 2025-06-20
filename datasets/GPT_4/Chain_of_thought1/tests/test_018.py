import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_all_positive(self): self.assertEqual(pos_count([1, 2, 3, 4]), 4)

    def test_mixed_numbers(self): self.assertEqual(pos_count([-2, 0, 4, -1, 3]), 2)

    def test_all_negative(self): self.assertEqual(pos_count([-1, -5, -100]), 0)

    def test_all_zeros(self): self.assertEqual(pos_count([0, 0, 0]), 0)

    def test_empty_list(self): self.assertEqual(pos_count([]), 0)

    def test_with_floats(self): self.assertEqual(pos_count([-1.5, 0.0, 2.3, 3.7]), 2)

    def test_with_booleans(self): self.assertEqual(pos_count([True, False, 1, 0]), 2)

    def test_single_positive(self): self.assertEqual(pos_count([100]), 1)

