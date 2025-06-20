import unittest
from datasets.mbpp.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_decimal_to_binary_with_8_expect_1000(self):
        self.assertEqual(decimal_to_binary(8), "1000")

    def test_decimal_to_binary_with_18_expect_10010(self):
        self.assertEqual(decimal_to_binary(18), "10010")

    def test_decimal_to_binary_with_7_expect_111(self):
        self.assertEqual(decimal_to_binary(7), "111")

