import unittest
from datasets.mbpp.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_multiply_int_with_10_20_expect_200(self):
        self.assertEqual(multiply_int(10,20), 200)

    def test_multiply_int_with_5_10_expect_50(self):
        self.assertEqual(multiply_int(5,10), 50)

    def test_multiply_int_with_4_8_expect_32(self):
        self.assertEqual(multiply_int(4,8), 32)

