import unittest
from datasets.o3.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_sorted_digits(self):
        self.assertEqual(find_Max_Num([1, 2, 3]), 321)

    def test_unsorted_digits(self):
        self.assertEqual(find_Max_Num([7, 8, 3, 5]), 8753)

    def test_with_zeros(self):
        self.assertEqual(find_Max_Num([0, 1, 2, 0]), 2100)

    def test_all_same_digits(self):
        self.assertEqual(find_Max_Num([9, 9, 9]), 999)

    def test_single_digit(self):
        self.assertEqual(find_Max_Num([5]), 5)

    def test_multi_digit_elements(self):
        self.assertEqual(find_Max_Num([34, 12, 5]), 3525)

