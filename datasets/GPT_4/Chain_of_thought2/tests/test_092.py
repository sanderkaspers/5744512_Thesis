import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_already_power_of_2(self): self.assertEqual(next_power_of_2(8), 8)

    def test_just_below_power_of_2(self): self.assertEqual(next_power_of_2(7), 8)

    def test_just_above_power_of_2(self): self.assertEqual(next_power_of_2(9), 16)

    def test_input_is_one(self): self.assertEqual(next_power_of_2(1), 1)

    def test_large_number(self): self.assertEqual(next_power_of_2(1000000), 1048576)

    def test_power_of_2_edge_case(self): self.assertEqual(next_power_of_2(1024), 1024)

