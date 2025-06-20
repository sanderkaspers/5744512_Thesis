import unittest
from datasets.mbpp.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_case(self):
        self.assertEqual(is_Diff(12345), False)

    def test_is_Diff_with_1212112_expect_True(self):
        self.assertEqual(is_Diff(1212112), True)

    def test_is_Diff_with_1212_expect_False(self):
        self.assertEqual(is_Diff(1212), False)

