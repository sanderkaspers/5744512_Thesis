import unittest
from datasets.GPT_4.Few_shot2.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_is_octagonal_n_1(self): self.assertEqual(is_octagonal(1), 1)

    def test_is_octagonal_n_2(self): self.assertEqual(is_octagonal(2), 6)

    def test_is_octagonal_n_3(self): self.assertEqual(is_octagonal(3), 15)

    def test_is_octagonal_n_10(self): self.assertEqual(is_octagonal(10), 280)

    def test_is_octagonal_n_0(self): self.assertEqual(is_octagonal(0), 0)

    def test_is_octagonal_negative_n(self): self.assertEqual(is_octagonal(-1), 5)

    def test_is_octagonal_large_n(self): self.assertEqual(is_octagonal(1000), 2998000)

