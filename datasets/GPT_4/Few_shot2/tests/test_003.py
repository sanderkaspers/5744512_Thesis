import unittest
from datasets.GPT_4.Few_shot2.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_find_Volume_normal_values(self): self.assertEqual(find_Volume(2, 3, 4), 12.0)

    def test_find_Volume_zero_length(self): self.assertEqual(find_Volume(0, 3, 4), 0.0)

    def test_find_Volume_zero_breadth(self): self.assertEqual(find_Volume(2, 0, 4), 0.0)

    def test_find_Volume_zero_height(self): self.assertEqual(find_Volume(2, 3, 0), 0.0)

    def test_find_Volume_all_zeros(self): self.assertEqual(find_Volume(0, 0, 0), 0.0)

    def test_find_Volume_negative_length(self): self.assertEqual(find_Volume(-2, 3, 4), -12.0)

    def test_find_Volume_negative_breadth(self): self.assertEqual(find_Volume(2, -3, 4), -12.0)

    def test_find_Volume_negative_height(self): self.assertEqual(find_Volume(2, 3, -4), -12.0)

    def test_find_Volume_all_negatives(self): self.assertEqual(find_Volume(-2, -3, -4), -12.0)

    def test_find_Volume_floats(self): self.assertEqual(find_Volume(2.5, 3.0, 4.0), 15.0)

