import unittest
from datasets.GPT_4.Few_shot.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(16), True) # Power of two)

    def test_case_2(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(3), True) # Sum of 1 (2^0) and 2 (2^1))

    def test_case_3(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(5), True) # Sum of 1 (2^0) and 4 (2^2))

    def test_case_4(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(7), True) # Sum of 1, 2, and 4)

    def test_case_5(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(1), True) # 1 is a power of two (2^0))

    def test_case_6(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True) # 2 + 8)

    def test_case_7(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(0), True) # Edge case, 0 can be considered as no sum)

    def test_case_8(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(6), True) # 2 + 4)

