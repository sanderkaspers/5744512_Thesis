import unittest
from datasets.GPT_4.Few_shot1.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_is_diff_divisible_positive(self): self.assertEqual(is_Diff(22), True)

    def test_is_diff_divisible_negative(self): self.assertEqual(is_Diff(-33), True)

    def test_is_diff_not_divisible(self): self.assertEqual(is_Diff(25), False)

    def test_is_diff_zero(self): self.assertEqual(is_Diff(0), True)

    def test_is_diff_large_multiple(self): self.assertEqual(is_Diff(110000), True)

    def test_is_diff_large_non_multiple(self): self.assertEqual(is_Diff(110001), False)

    def test_is_diff_near_multiple(self): self.assertEqual(is_Diff(121), True)

    def test_is_diff_just_under_multiple(self): self.assertEqual(is_Diff(120), False)

