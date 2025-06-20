import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_positive_numbers(self): self.assertEqual(max_Abs_Diff([1, 5, 9, 3]), 8)

    def test_all_identical_elements(self): self.assertEqual(max_Abs_Diff([4, 4, 4, 4]), 0)

    def test_sorted_ascending(self): self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 4)

    def test_sorted_descending(self): self.assertEqual(max_Abs_Diff([9, 7, 5, 3, 1]), 8)

    def test_negative_and_positive(self): self.assertEqual(max_Abs_Diff([-10, 0, 10]), 20)

    def test_two_elements(self): self.assertEqual(max_Abs_Diff([100, -100]), 200)

    def test_single_element(self): self.assertEqual(max_Abs_Diff([42]), 0)

    def test_floats(self): self.assertAlmostEqual(max_Abs_Diff([1.1, 2.5, -3.0]), 5.5)

    def test_large_list(self): self.assertEqual(max_Abs_Diff(list(range(-1000, 1001))), 2000)

