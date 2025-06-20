import unittest
from datasets.mbpp.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_count_Substrings_with_112112_6_expect_6(self):
        self.assertEqual(count_Substrings('112112'), 6)

    def test_count_Substrings_with_111_3_expect_6(self):
        self.assertEqual(count_Substrings('111'), 6)

    def test_count_Substrings_with_1101112_7_expect_12(self):
        self.assertEqual(count_Substrings('1101112'), 12)

