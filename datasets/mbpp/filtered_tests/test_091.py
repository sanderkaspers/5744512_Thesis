import unittest
from datasets.mbpp.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_find_even_pair_with_5_4_7_2_1_expect_4(self):
        self.assertEqual(find_even_pair([5,4,7,2,1]), 4)

    def test_find_even_pair_with_7_2_8_1_0_5_11_expect_9(self):
        self.assertEqual(find_even_pair([7,2,8,1,0,5,11]), 9)

    def test_find_even_pair_with_1_2_3_expect_1(self):
        self.assertEqual(find_even_pair([1,2,3]), 1)

