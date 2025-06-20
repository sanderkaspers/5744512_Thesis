import unittest
from datasets.mbpp.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_count_with_True_False_True_expect_2(self):
        self.assertEqual(count([True,False,True]), 2)

    def test_count_with_False_False_expect_0(self):
        self.assertEqual(count([False,False]), 0)

    def test_count_with_True_True_True_expect_3(self):
        self.assertEqual(count([True,True,True]), 3)

