import unittest
from datasets.mbpp.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_is_octagonal_with_5_expect_65(self):
        self.assertEqual(is_octagonal(5), 65)

    def test_is_octagonal_with_10_expect_280(self):
        self.assertEqual(is_octagonal(10), 280)

    def test_is_octagonal_with_15_expect_645(self):
        self.assertEqual(is_octagonal(15), 645)

