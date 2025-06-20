import unittest
from datasets.GPT_4.Few_shot2.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_next_power_of_2_exact_power(self): self.assertEqual(next_power_of_2(8), 8)

    def test_next_power_of_2_next_power(self): self.assertEqual(next_power_of_2(9), 16)

    def test_next_power_of_2_below_first_power(self): self.assertEqual(next_power_of_2(1), 1)

    def test_next_power_of_2_zero(self): self.assertEqual(next_power_of_2(0), 1)

    def test_next_power_of_2_between_powers(self): self.assertEqual(next_power_of_2(5), 8)

    def test_next_power_of_2_large_number(self): self.assertEqual(next_power_of_2(130), 256)

    def test_next_power_of_2_just_below_power(self): self.assertEqual(next_power_of_2(15), 16)

    def test_next_power_of_2_just_above_power(self): self.assertEqual(next_power_of_2(17), 32)

    def test_next_power_of_2_already_power(self): self.assertEqual(next_power_of_2(64), 64)

