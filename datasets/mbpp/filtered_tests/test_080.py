import unittest
from datasets.mbpp.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(extract_singly([[3, 4, 5], [4, 5], [5, 6]]), [3, 4, 5, 6])

    def test_case_2(self):
        self.assertEqual(extract_singly([[1, 2], [2, 3], [3, 4]]), [1, 2, 3, 4])

    def test_case_3(self):
        self.assertEqual(extract_singly([[7, 8], [8, 9], [9, 10]]), [7, 8, 9, 10])

