import unittest
from datasets.GPT_4.Few_shot2.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_hexagonal_num_1(self): self.assertEqual(hexagonal_num(1), 1)

    def test_hexagonal_num_2(self): self.assertEqual(hexagonal_num(2), 6)

    def test_hexagonal_num_3(self): self.assertEqual(hexagonal_num(3), 15)

    def test_hexagonal_num_5(self): self.assertEqual(hexagonal_num(5), 45)

    def test_hexagonal_num_10(self): self.assertEqual(hexagonal_num(10), 190)

    def test_hexagonal_num_0(self): self.assertEqual(hexagonal_num(0), 0)

    def test_hexagonal_num_negative(self): self.assertEqual(hexagonal_num(-1), -1)

    def test_hexagonal_num_large(self): self.assertEqual(hexagonal_num(100), 19800)

