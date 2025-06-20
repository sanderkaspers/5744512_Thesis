import unittest
from datasets.mbpp.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_add_lists_with_5_6_7__9_10__expect__9(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

    def test_add_lists_with_6_7_8__10_11__expect__10(self):
        self.assertEqual(add_lists([6, 7, 8], (10, 11)), (10, 11, 6, 7, 8))

    def test_add_lists_with_7_8_9__11_12__expect__11(self):
        self.assertEqual(add_lists([7, 8, 9], (11, 12)), (11, 12, 7, 8, 9))

