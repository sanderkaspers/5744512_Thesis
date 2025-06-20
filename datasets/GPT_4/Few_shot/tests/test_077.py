import unittest
from datasets.GPT_4.Few_shot.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(zero_count(array('i', [1, 2, 3, 4])), 0) # No zeros)

    def test_case_2(self):
        self.assertEqual(zero_count(array('i', [0, 0, 0])), 3) # All zeros)

    def test_case_3(self):
        self.assertEqual(zero_count(array('i', [1, 0, 2, 0, 3, 0])), 3) # Mixed with zeros and non-zeros)

    def test_case_4(self):
        self.assertEqual(zero_count(array('i', [])), 0) # Empty array)

    def test_case_5(self):
        self.assertEqual(zero_count(array('i', [0])), 1) # Single zero)

    def test_case_6(self):
        self.assertEqual(zero_count(array('i', [0, 1, 0, 2, 0, 3, 4, 0])), 4) # Mixed with zeros spread out)

    def test_case_7(self):
        self.assertEqual(zero_count(array('i', [10, 20, 30, 40, 50])), 0) # No zeros, all positive numbers)

    def test_case_8(self):
        self.assertEqual(zero_count(array('i', [-10, 0, 20, 0])), 2) # Mixed with negative and zero)

