import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Max_Num([1, 3, 7, 4]), 7431)

    def test_single_digit(self):
        self.assertEqual(find_Max_Num([5]), 5)

    def test_all_identical_digits(self):
        self.assertEqual(find_Max_Num([2, 2, 2, 2]), 2222)

    def test_list_with_zeros(self):
        self.assertEqual(find_Max_Num([0, 5, 0]), 500)

    def test_descending_order(self):
        self.assertEqual(find_Max_Num([9, 8, 7, 6]), 9876)

    def test_ascending_order(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4]), 4321)

    def test_empty_list(self):
        self.assertEqual(find_Max_Num([]), 0)

    def test_large_list(self):
        self.assertEqual(find_Max_Num([1] * 100), int('1' * 100))

    def test_negative_digits(self):
        with self.assertRaises(ValueError):
            find_Max_Num([-1, -3, -7])

    def test_floating_point_numbers(self):
        with self.assertRaises(TypeError):
            find_Max_Num([1.2, 3.4, 5.6])

    def test_mixed_content_list(self):
        with self.assertRaises(TypeError):
            find_Max_Num([1, '2', 3])

    def test_max_min_digits_only(self):
        self.assertEqual(find_Max_Num([0, 9, 9, 0]), 9900)

    def test_repeated_digits(self):
        self.assertEqual(find_Max_Num([1, 1, 1, 1]), 1111)

    def test_all_zeros(self):
        self.assertEqual(find_Max_Num([0, 0, 0]), 0)

