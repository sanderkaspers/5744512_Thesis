import unittest
from datasets.mbpp.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_search_with_1_1_2_2_3_expect_3(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

    def test_search_with_1_1_3_3_4_4_5_5_7_7_8_expect_8(self):
        self.assertEqual(search([1,1,3,3,4,4,5,5,7,7,8]), 8)

    def test_search_with_1_2_2_3_3_4_4_expect_1(self):
        self.assertEqual(search([1,2,2,3,3,4,4]), 1)

