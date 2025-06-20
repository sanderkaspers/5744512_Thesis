import unittest
from datasets.GPT_4.Few_shot.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 3), 7) # Normal case)

    def test_case_2(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 1), 3) # k = 1 (smallest element))

    def test_case_3(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6), 20) # k = n (largest element))

    def test_case_4(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 5) # Already sorted array)

    def test_case_5(self):
        self.assertEqual(kth_element([9, 8, 7, 6, 5, 4, 3, 2, 1], 5), 5) # Reverse sorted array)

    def test_case_6(self):
        self.assertEqual(kth_element([1, 1, 1, 1, 1, 1], 3), 1) # All elements same)

    def test_case_7(self):
        self.assertEqual(kth_element([12, 3, 5, 7, 19], 2), 5) # Short array)

    def test_case_8(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 4), 10) # Mixed array)

