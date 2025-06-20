import unittest
from datasets.GPT_4.Few_shot.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4) # Ascending order)

    def test_case_2(self):
        self.assertEqual(max_difference([5, 4, 3, 2, 1]), 4) # Descending order)

    def test_case_3(self):
        self.assertEqual(max_difference([-1, -2, -3, -4, -5]), 4) # All negative numbers)

    def test_case_4(self):
        self.assertEqual(max_difference([100, 99, 98, 97, 96]), 4) # Small range of values)

    def test_case_5(self):
        self.assertEqual(max_difference([10, 20, 30, 40, 50]), 40) # Larger range of values)

    def test_case_6(self):
        self.assertEqual(max_difference([3, 3, 3, 3, 3]), 0) # All identical elements)

    def test_case_7(self):
        self.assertEqual(max_difference([2, -3, 4, -1, 5, -6]), 10) # Mix of positive and negative numbers)

    def test_case_8(self):
        self.assertEqual(max_difference([1]), 0) # Single element)

