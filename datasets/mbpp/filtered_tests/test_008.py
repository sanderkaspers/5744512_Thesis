import unittest
from datasets.mbpp.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_is_woodall_with_383_expect_True(self):
        self.assertEqual(is_woodall(383), True)

    def test_is_woodall_with_254_expect_False(self):
        self.assertEqual(is_woodall(254), False)

    def test_is_woodall_with_200_expect_False(self):
        self.assertEqual(is_woodall(200), False)

