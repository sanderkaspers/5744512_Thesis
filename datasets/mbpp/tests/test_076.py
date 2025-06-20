import unittest
from datasets.mbpp.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_hexagonal_num_with_10_expect_190(self):
        self.assertEqual(hexagonal_num(10), 190)

    def test_hexagonal_num_with_5_expect_45(self):
        self.assertEqual(hexagonal_num(5), 45)

    def test_hexagonal_num_with_7_expect_91(self):
        self.assertEqual(hexagonal_num(7), 91)

