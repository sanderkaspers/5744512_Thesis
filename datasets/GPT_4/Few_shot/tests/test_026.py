import unittest
from datasets.GPT_4.Few_shot.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_tuples([(1, 2), (3, 4), (5, 5)], 5), [(1, 2)]) # Single match)

    def test_case_2(self):
        self.assertEqual(find_tuples([(1, 2), (2, 3), (3, 4)], 5), [(1, 2), (2, 3)]) # Multiple matches)

    def test_case_3(self):
        self.assertEqual(find_tuples([(1, 2), (2, 2), (3, 4)], 6), [(3, 4)]) # One match)

    def test_case_4(self):
        self.assertEqual(find_tuples([(1, 2), (2, 2), (3, 3)], 10), []) # No match)

    def test_case_5(self):
        self.assertEqual(find_tuples([], 5), []) # Empty list)

    def test_case_6(self):
        self.assertEqual(find_tuples([(1,), (1, 2), (2, 3)], 3), [(1, 2)]) # Tuples of varying lengths)

    def test_case_7(self):
        self.assertEqual(find_tuples([(1, 2), (-1, -2), (3, 4)], 3), [(1, 2), (-1, -2)]) # With negative numbers)

    def test_case_8(self):
        self.assertEqual(find_tuples([(0, 5), (5, 0), (2, 3)], 5), [(0, 5), (5, 0), (2, 3)]) # Multiple tuples with same sum)

