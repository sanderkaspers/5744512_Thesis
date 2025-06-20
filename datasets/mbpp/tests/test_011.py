import unittest
from datasets.mbpp.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_opposite_Signs_with_1__2_expect_True(self):
        self.assertEqual(opposite_Signs(1,-2), True)

    def test_opposite_Signs_with_3_2_expect_False(self):
        self.assertEqual(opposite_Signs(3,2), False)

    def test_opposite_Signs_with__10__10_expect_False(self):
        self.assertEqual(opposite_Signs(-10,-10), False)

