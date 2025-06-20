import unittest
from datasets.GPT_4.Few_shot2.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_smallest_num_basic(self): self.assertEqual(smallest_num([3, 1, 2]), 1)

    def test_smallest_num_all_same(self): self.assertEqual(smallest_num([4, 4, 4]), 4)

    def test_smallest_num_negative_values(self): self.assertEqual(smallest_num([-1, -2, -3]), -3)

    def test_smallest_num_mixed_values(self): self.assertEqual(smallest_num([-10, 0, 10]), -10)

    def test_smallest_num_single_element(self): self.assertEqual(smallest_num([8]), 8)

    def test_smallest_num_floats(self): self.assertEqual(smallest_num([1.1, 0.5, 3.3]), 0.5)

    def test_smallest_num_min_at_end(self): self.assertEqual(smallest_num([5, 6, 1]), 1)

    def test_smallest_num_min_at_start(self): self.assertEqual(smallest_num([0, 4, 8]), 0)

