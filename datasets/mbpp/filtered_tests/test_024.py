import unittest
from datasets.mbpp.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_dif_Square_with_5_expect_True(self):
        self.assertEqual(dif_Square(5), True)

    def test_dif_Square_with_10_expect_False(self):
        self.assertEqual(dif_Square(10), False)

    def test_dif_Square_with_15_expect_True(self):
        self.assertEqual(dif_Square(15), True)

