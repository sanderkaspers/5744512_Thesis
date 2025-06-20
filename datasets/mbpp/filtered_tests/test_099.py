import unittest
from datasets.mbpp.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_count_Set_Bits_with_2_expect_1(self):
        self.assertEqual(count_Set_Bits(2), 1)

    def test_count_Set_Bits_with_4_expect_1(self):
        self.assertEqual(count_Set_Bits(4), 1)

    def test_count_Set_Bits_with_6_expect_2(self):
        self.assertEqual(count_Set_Bits(6), 2)

