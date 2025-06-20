import unittest
from datasets.GPT_4.Few_shot1.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_next_power_of_2_zero(self): self.assertEqual(next_power_of_2(0), 1)

    def test_next_power_of_2_one(self): self.assertEqual(next_power_of_2(1), 1)

    def test_next_power_of_2_two(self): self.assertEqual(next_power_of_2(2), 2)

    def test_next_power_of_2_three(self): self.assertEqual(next_power_of_2(3), 4)

    def test_next_power_of_2_four(self): self.assertEqual(next_power_of_2(4), 4)

    def test_next_power_of_2_five(self): self.assertEqual(next_power_of_2(5), 8)

    def test_next_power_of_2_seven(self): self.assertEqual(next_power_of_2(7), 8)

    def test_next_power_of_2_eight(self): self.assertEqual(next_power_of_2(8), 8)

    def test_next_power_of_2_nine(self): self.assertEqual(next_power_of_2(9), 16)

    def test_next_power_of_2_fifteen(self): self.assertEqual(next_power_of_2(15), 16)

    def test_next_power_of_2_sixteen(self): self.assertEqual(next_power_of_2(16), 16)

    def test_next_power_of_2_large(self): self.assertEqual(next_power_of_2(12345), 16384)

    def test_next_power_of_2_power_minus_one(self): self.assertEqual(next_power_of_2(31), 32)

    def test_next_power_of_2_power_plus_one(self): self.assertEqual(next_power_of_2(33), 64)

    def test_next_power_of_2_negative(self): ):     self.fail("Negative input not supported by implementation; test would hang.") # self.assertEqual(next_power_of_2(-1), 1)

    def test_next_power_of_2_negative_large(self): ):     self.fail("Negative input not supported by implementation; test would hang.") # self.assertEqual(next_power_of_2(-123), 1)

    def test_next_power_of_2_already_power_of_2_large(self): self.assertEqual(next_power_of_2(1024), 1024)

    def test_next_power_of_2_edge_case(self): self.assertEqual(next_power_of_2(1023), 1024)

