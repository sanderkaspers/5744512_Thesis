import unittest
from datasets.GPT_4.Few_shot1.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_closest_num_positive(self): self.assertEqual(closest_num(10), 9)

    def test_closest_num_one(self): self.assertEqual(closest_num(1), 0)

    def test_closest_num_zero(self): self.assertEqual(closest_num(0), -1)

    def test_closest_num_negative(self): self.assertEqual(closest_num(-5), -6)

    def test_closest_num_large(self): self.assertEqual(closest_num(1000000), 999999)

