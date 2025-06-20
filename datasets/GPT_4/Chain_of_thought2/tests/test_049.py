import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_first_element(self): self.assertEqual(kth_element([3, 1, 2], 1), 1)

    def test_middle_element(self): self.assertEqual(kth_element([10, 30, 20, 40], 2), 20)

    def test_duplicates(self): self.assertEqual(kth_element([4, 4, 4, 4], 3), 4)

    def test_all_identical(self): self.assertEqual(kth_element([7, 7, 7, 7, 7], 5), 7)

    def test_largest_element(self): self.assertEqual(kth_element([5, 3, 9, 1], 4), 9)

    def test_negative_and_positive_numbers(self): self.assertEqual(kth_element([0, -5, 2, -3, 4], 2), -3)

