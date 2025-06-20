import unittest
from datasets.mbpp.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_case(self):
        self.assertEqual(find_tuples([(6, 24, 12), (5, 10, 15)], 6), [(6, 24, 12)])

    def test_case(self):
        self.assertEqual(find_tuples([(5, 25, 30), (7, 8, 9)], 5), [(5, 25, 30)])

    def test_case(self):
        self.assertEqual(find_tuples([(7, 9, 16), (8, 16, 24)], 8), [(8, 16, 24)])

