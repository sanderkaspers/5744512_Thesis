import unittest
from datasets.mbpp.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_check_type_with__5_6_7_3_5_6__expect_True(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

    def test_check_type_with__1_2__4__expect_False(self):
        self.assertEqual(check_type((1, 2, "4")), False)

    def test_check_type_with__3_2_1_4_5__expect_True(self):
        self.assertEqual(check_type((3, 2, 1, 4, 5)), True)

