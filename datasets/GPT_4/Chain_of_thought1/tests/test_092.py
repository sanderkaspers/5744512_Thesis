import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_power_of_2(self): self.assertEqual(next_power_of_2(8), 8)

    def test_one(self): self.assertEqual(next_power_of_2(1), 1)

    def test_three(self): self.assertEqual(next_power_of_2(3), 4)

    def test_five(self): self.assertEqual(next_power_of_2(5), 8)

    def test_seventeen(self): self.assertEqual(next_power_of_2(17), 32)

    def test_thirty_one(self): self.assertEqual(next_power_of_2(31), 32)

    def test_sixty_four(self): self.assertEqual(next_power_of_2(64), 64)

    def test_sixty_five(self): self.assertEqual(next_power_of_2(65), 128)

    def test_zero(self): self.assertEqual(next_power_of_2(0), 1)

    def test_large_input(self): self.assertEqual(next_power_of_2(1025), 2048)

    def test_negative_input(self): self.fail("Negative input not supported by implementation; test would hang.") #    with self.assertRaises(ValueError): #self.assertEqual(next_power_of_2(-5), 1)

    def test_boolean_input(self): self.assertEqual(next_power_of_2(True), 1)

