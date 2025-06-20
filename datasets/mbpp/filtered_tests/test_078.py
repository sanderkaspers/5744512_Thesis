import unittest
from datasets.mbpp.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_is_Sum_Of_Powers_Of_Two_with_10_expect_True(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

    def test_is_Sum_Of_Powers_Of_Two_with_7_expect_False(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(7), False)

    def test_is_Sum_Of_Powers_Of_Two_with_14_expect_True(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(14), True)

