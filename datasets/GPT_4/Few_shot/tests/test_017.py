import unittest
from datasets.GPT_4.Few_shot.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15) # Simple list)

    def test_case_2(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], [4, 5]]), 15) # Nested list)

    def test_case_3(self):
        self.assertEqual(recursive_list_sum([[1, 2, [3]], 4, 5]), 15) # Deeply nested list)

    def test_case_4(self):
        self.assertEqual(recursive_list_sum([[-1, -2, [-3]], 4, 5]), 3) # Nested list with negative numbers)

    def test_case_5(self):
        self.assertEqual(recursive_list_sum([]), 0) # Empty list)

    def test_case_6(self):
        self.assertEqual(recursive_list_sum([[[]]]), 0) # Empty nested list)

    def test_case_7(self):
        self.assertEqual(recursive_list_sum([1, [2], [[3], [4]], 5]), 15) # Multiple levels of nesting)

    def test_case_8(self):
        self.assertEqual(recursive_list_sum([0, [0, [0]], 0]), 0) # List with zeros)

