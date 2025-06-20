import unittest
from datasets.mbpp.programs.program_067 import *

class TestVersion(unittest.TestCase):
    def test_find_length_with__11000010001__11_expect_6(self):
        self.assertEqual(find_length("11000010001"), 6)

    def test_find_length_with__10111__5_expect_1(self):
        self.assertEqual(find_length("10111"), 1)

    def test_find_length_with__11011101100101__14_expect_2(self):
        self.assertEqual(find_length("11011101100101"), 2)

