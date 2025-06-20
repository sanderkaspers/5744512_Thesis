import unittest
from datasets.GPT_4.Few_shot1.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_hexagonal_num_first(self): self.assertEqual(hexagonal_num(1), 1)

    def test_hexagonal_num_small(self): self.assertEqual(hexagonal_num(2), 6)

    def test_hexagonal_num_medium(self): self.assertEqual(hexagonal_num(5), 45)

    def test_hexagonal_num_large(self): self.assertEqual(hexagonal_num(10), 190)

    def test_hexagonal_num_zero(self): self.assertEqual(hexagonal_num(0), 0)

    def test_hexagonal_num_negative_one(self): self.assertEqual(hexagonal_num(-1), -1)

    def test_hexagonal_num_negative_two(self): self.assertEqual(hexagonal_num(-2), -6)

    def test_hexagonal_num_negative_five(self): self.assertEqual(hexagonal_num(-5), -45)

    def test_hexagonal_num_large_negative(self): self.assertEqual(hexagonal_num(-10), -190)

