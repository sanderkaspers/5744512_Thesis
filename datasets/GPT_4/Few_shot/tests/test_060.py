import unittest
from datasets.GPT_4.Few_shot.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123) # Positive digits)

    def test_case_2(self):
        self.assertEqual(tuple_to_int((0, 0, 1)), 1) # Leading zeros)

    def test_case_3(self):
        self.assertEqual(tuple_to_int(()), 0) # Empty tuple)

    def test_case_4(self):
        self.assertEqual(tuple_to_int((5,)), 5) # Single-element tuple)

    def test_case_5(self):
        self.assertEqual(tuple_to_int((0, 0, 0)), 0) # All zeros)

    def test_case_6(self):
        self.assertEqual(tuple_to_int((1, 0, 2)), 102) # Mixed zeros and digits)

    def test_case_7(self):
        self.assertEqual(tuple_to_int((9, 9, 9)), 999) # All same digits)

    def test_case_8(self):
        self.assertEqual(tuple_to_int((7, 0, 8, 0)), 7080) # Alternating digits and zeros)

