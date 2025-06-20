import unittest
from datasets.mbpp.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_case(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

    def test_case(self):
        self.assertEqual(max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]), 15)

    def test_case(self):
        self.assertEqual(max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]), 23)

