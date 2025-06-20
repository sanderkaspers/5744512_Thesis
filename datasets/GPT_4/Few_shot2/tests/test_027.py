import unittest
from datasets.GPT_4.Few_shot2.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_is_Diff_divisible_by_11(self): self.assertTrue(is_Diff(22))

    def test_is_Diff_not_divisible_by_11(self): self.assertFalse(is_Diff(23))

    def test_is_Diff_zero(self): self.assertTrue(is_Diff(0))

    def test_is_Diff_negative_divisible(self): self.assertTrue(is_Diff(-33))

    def test_is_Diff_negative_not_divisible(self): self.assertFalse(is_Diff(-20))

