import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_all_positive(self): self.assertEqual(find_Max_Num([1, 2, 3, 4, 5]), 5)

    def test_mixed_signs(self): self.assertEqual(find_Max_Num([-10, 4, 2, -3]), 4)

    def test_all_negative(self): self.assertEqual(find_Max_Num([-10, -20, -3, -4]), -3)

    def test_float_and_int(self): self.assertEqual(find_Max_Num([1.5, 2, 3.2, 2.1]), 3.2)

    def test_max_at_start(self): self.assertEqual(find_Max_Num([100, 50, 20]), 100)

    def test_max_at_end(self): self.assertEqual(find_Max_Num([1, 5, 7, 99]), 99)

    def test_duplicate_max(self): self.assertEqual(find_Max_Num([1, 3, 3, 2]), 3)

    def test_single_element(self): self.assertEqual(find_Max_Num([42]), 42)

