import unittest
from datasets.GPT_4.Few_shot2.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_max_difference_basic(self): self.assertEqual(max_difference([1, 5, 9]), 4)

    def test_max_difference_negative_values(self): self.assertEqual(max_difference([-1, -5, -3]), 4)

    def test_max_difference_mixed_values(self): self.assertEqual(max_difference([-10, 0, 10]), 10)

    def test_max_difference_single_jump_large(self): self.assertEqual(max_difference([1, 100]), 99)

    def test_max_difference_all_equal(self): self.assertEqual(max_difference([5, 5, 5]), 0)

    def test_max_difference_descending(self): self.assertEqual(max_difference([10, 7, 1]), 6)

    def test_max_difference_floats(self): self.assertEqual(max_difference([1.5, 3.7, 2.2]), 2.2)

    def test_max_difference_two_elements(self): self.assertEqual(max_difference([3, 7]), 4)

