import unittest
from datasets.mbpp.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_find_solution_with_2_3_7_expect__2(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

    def test_case(self):
        self.assertIsNone(find_solution(4, 2, 7))

    def test_find_solution_with_1_13_17_expect__4(self):
        self.assertEqual(find_solution(1, 13, 17), (4, 1))

