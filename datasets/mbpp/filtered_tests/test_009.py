import unittest
from datasets.mbpp.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_check_with_70_expect_False(self):
        self.assertEqual(check(70), False)

    def test_check_with_23_expect_False(self):
        self.assertEqual(check(23), False)

    def test_check_with_73_expect_True(self):
        self.assertEqual(check(73), True)

