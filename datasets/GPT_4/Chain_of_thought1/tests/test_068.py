import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_normal_range(self): self.assertEqual(sum(1, 5), 15)

    def test_same_values(self): self.assertEqual(sum(3, 3), 3)

    def test_zero_values(self): self.assertEqual(sum(0, 0), 0)

    def test_negative_to_positive(self): self.assertEqual(sum(-3, 3), 0)

    def test_all_negative(self): self.assertEqual(sum(-5, -1), -15)

    def test_range_with_zero(self): self.assertEqual(sum(0, 5), 15)

    def test_reversed_range(self): self.assertEqual(sum(5, 1), 0)

    def test_large_input(self): self.assertEqual(sum(1, 1000), 500500)

