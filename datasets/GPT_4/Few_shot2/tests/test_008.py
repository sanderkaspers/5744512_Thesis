import unittest
from datasets.GPT_4.Few_shot2.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_is_woodall_known_woodall_number(self): self.assertTrue(is_woodall(17))

    def test_is_woodall_another_valid_case(self): self.assertTrue(is_woodall(4097))

    def test_is_woodall_zero(self): self.assertFalse(is_woodall(0))

    def test_is_woodall_one(self): self.assertFalse(is_woodall(1))

    def test_is_woodall_even_number(self): self.assertFalse(is_woodall(16))

    def test_is_woodall_not_woodall(self): self.assertFalse(is_woodall(20))

    def test_is_woodall_large_false(self): self.assertFalse(is_woodall(100000))

    def test_is_woodall_large_true(self): self.assertTrue(is_woodall(2049))

    def test_is_woodall_negative_number(self): self.assertFalse(is_woodall(-17))

