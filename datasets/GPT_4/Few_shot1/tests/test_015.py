import unittest
from datasets.GPT_4.Few_shot1.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_max_difference_basic(self): self.assertEqual(max_difference([1, 2, 3, 5]), 2)

    def test_max_difference_two_elements(self): self.assertEqual(max_difference([10, 4]), 6)

    def test_max_difference_all_same(self): self.assertEqual(max_difference([7, 7, 7]), 0)

    def test_max_difference_with_negatives(self): self.assertEqual(max_difference([-10, -20, -30]), 10)

    def test_max_difference_mixed_values(self): self.assertEqual(max_difference([5, -5, 15]), 20)

    def test_max_difference_large_input(self): self.assertEqual(max_difference(list(range(1000))), 1)

    def test_max_difference_descending(self): self.assertEqual(max_difference([100, 90, 70, 60]), 20)

    def test_max_difference_zeroes(self): self.assertEqual(max_difference([0, 0, 0, 0]), 0)

