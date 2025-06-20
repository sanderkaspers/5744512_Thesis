import unittest
from datasets.mbpp.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_pos_count_with_1__2_3__4_expect_2(self):
        self.assertEqual(pos_count([1,-2,3,-4]), 2)

    def test_pos_count_with_3_4_5__1_expect_3(self):
        self.assertEqual(pos_count([3,4,5,-1]), 3)

    def test_pos_count_with_1_2_3_4_expect_4(self):
        self.assertEqual(pos_count([1,2,3,4]), 4)

