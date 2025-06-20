import unittest
from datasets.GPT_4.Few_shot1.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_smallest_num_single_element(self): self.assertEqual(smallest_num([7]), 7)

    def test_smallest_num_all_positive(self): self.assertEqual(smallest_num([3, 6, 2, 9]), 2)

    def test_smallest_num_all_negative(self): self.assertEqual(smallest_num([-5, -9, -2]), -9)

    def test_smallest_num_mixed_values(self): self.assertEqual(smallest_num([-3, 0, 5, -1]), -3)

    def test_smallest_num_all_same(self): self.assertEqual(smallest_num([4, 4, 4]), 4)

    def test_smallest_num_with_floats(self): self.assertEqual(smallest_num([2.5, 3.1, 1.9]), 1.9)

    def test_smallest_num_large_input(self): self.assertEqual(smallest_num(list(range(10000, -10000, -1))), -9999)

