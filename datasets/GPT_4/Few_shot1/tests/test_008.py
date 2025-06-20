import unittest
from datasets.GPT_4.Few_shot1.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_is_woodall_known_woodall(self): self.assertEqual(is_woodall(17), True)

    def test_is_woodall_smallest_woodall(self): self.assertEqual(is_woodall(1), True)

    def test_is_woodall_even_number(self): self.assertEqual(is_woodall(8), False)

    def test_is_woodall_non_woodall_odd(self): self.assertEqual(is_woodall(9), False)

    def test_is_woodall_large_woodall(self): self.assertEqual(is_woodall(2049), True)

    def test_is_woodall_large_non_woodall(self): self.assertEqual(is_woodall(2050), False)

    def test_is_woodall_zero(self): self.assertEqual(is_woodall(0), False)

    def test_is_woodall_negative_number(self): ):     self.fail("Negative input not supported by implementation; test would hang.") # self.assertEqual(is_woodall(-1), False)

