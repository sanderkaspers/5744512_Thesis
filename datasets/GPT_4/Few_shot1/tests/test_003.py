import unittest
from datasets.GPT_4.Few_shot1.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_find_volume_positive_integers(self): self.assertEqual(find_Volume(2, 3, 4), 24)

    def test_find_volume_zero_dimension(self): self.assertEqual(find_Volume(0, 3, 4), 0)

    def test_find_volume_all_zeros(self): self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_find_volume_one_dimension_one(self): self.assertEqual(find_Volume(1, 3, 4), 12)

    def test_find_volume_negative_dimension(self): self.assertEqual(find_Volume(-2, 3, 4), -24)

    def test_find_volume_all_negative(self): self.assertEqual(find_Volume(-2, -3, -4), -24)

    def test_find_volume_floats_as_integers(self): self.assertEqual(find_Volume(2.5, 2, 2), 10.0)

    def test_find_volume_large_numbers(self): self.assertEqual(find_Volume(100000, 200000, 300000), 6000000000000000)

    def test_find_volume_single_dimension_large(self): self.assertEqual(find_Volume(1, 1, 1000000), 1000000)

