import unittest
from datasets.GPT_4.Few_shot1.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_is_octagonal_n_zero(self): self.assertEqual(is_octagonal(0), 0)

    def test_is_octagonal_n_one(self): self.assertEqual(is_octagonal(1), 1)

    def test_is_octagonal_n_two(self): self.assertEqual(is_octagonal(2), 10)

    def test_is_octagonal_n_five(self): self.assertEqual(is_octagonal(5), 65)

    def test_is_octagonal_large_n(self): self.assertEqual(is_octagonal(100), 29800)

    def test_is_octagonal_negative_n(self): self.assertEqual(is_octagonal(-1), -5)

