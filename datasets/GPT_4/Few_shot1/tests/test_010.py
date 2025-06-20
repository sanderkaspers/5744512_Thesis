import unittest
from datasets.GPT_4.Few_shot1.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_find_max_num_single_element(self): self.assertEqual(find_Max_Num([5]), 5)

    def test_find_max_num_two_elements(self): self.assertEqual(find_Max_Num([3, 7]), 7)

    def test_find_max_num_sorted_ascending(self): self.assertEqual(find_Max_Num([1, 2, 3, 4, 5]), 5)

    def test_find_max_num_sorted_descending(self): self.assertEqual(find_Max_Num([5, 4, 3, 2, 1]), 5)

    def test_find_max_num_all_same(self): self.assertEqual(find_Max_Num([4, 4, 4, 4]), 4)

    def test_find_max_num_negative_values(self): self.assertEqual(find_Max_Num([-10, -5, -20]), -5)

    def test_find_max_num_mixed_values(self): self.assertEqual(find_Max_Num([-10, 0, 10, -5]), 10)

    def test_find_max_num_floats(self): self.assertEqual(find_Max_Num([1.5, 2.3, 0.7]), 2.3)

    def test_find_max_num_large_input(self): self.assertEqual(find_Max_Num(list(range(10000))), 9999)

