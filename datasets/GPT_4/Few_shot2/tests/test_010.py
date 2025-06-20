import unittest
from datasets.GPT_4.Few_shot2.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_find_Max_Num_basic(self): self.assertEqual(find_Max_Num([1, 2, 3]), 3)

    def test_find_Max_Num_descending(self): self.assertEqual(find_Max_Num([3, 2, 1]), 3)

    def test_find_Max_Num_all_equal(self): self.assertEqual(find_Max_Num([5, 5, 5]), 5)

    def test_find_Max_Num_negative_values(self): self.assertEqual(find_Max_Num([-1, -3, -2]), -1)

    def test_find_Max_Num_mixed_values(self): self.assertEqual(find_Max_Num([-10, 0, 10]), 10)

    def test_find_Max_Num_large_list(self): self.assertEqual(find_Max_Num(list(range(10000))), 9999)

    def test_find_Max_Num_single_element(self): self.assertEqual(find_Max_Num([7]), 7)

    def test_find_Max_Num_float_values(self): self.assertEqual(find_Max_Num([1.1, 2.2, 3.3]), 3.3)

    def test_find_Max_Num_max_at_start(self): self.assertEqual(find_Max_Num([100, 20, 30]), 100)

    def test_find_Max_Num_max_at_end(self): self.assertEqual(find_Max_Num([1, 2, 300]), 300)

