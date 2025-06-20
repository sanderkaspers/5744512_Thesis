import unittest
from datasets.GPT_4.Few_shot2.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_divisor_n_is_1(self): self.assertEqual(divisor(1), 0)

    def test_divisor_n_is_2(self): self.assertEqual(divisor(2), 1)

    def test_divisor_n_is_3(self): self.assertEqual(divisor(3), 2)

    def test_divisor_n_is_4(self): self.assertEqual(divisor(4), 0)

    def test_divisor_n_is_large(self): self.assertEqual(divisor(100), 99 % 3)

