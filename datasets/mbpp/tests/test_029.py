import unittest
from datasets.mbpp.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_tetrahedral_number_with_5_expect_35_0(self):
        self.assertEqual(tetrahedral_number(5), 35.0)

    def test_tetrahedral_number_with_6_expect_56_0(self):
        self.assertEqual(tetrahedral_number(6), 56.0)

    def test_tetrahedral_number_with_7_expect_84_0(self):
        self.assertEqual(tetrahedral_number(7), 84.0)

