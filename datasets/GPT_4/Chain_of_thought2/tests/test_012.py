import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_max_first(self): self.assertEqual(max_of_three(9, 3, 5), 9)

    def test_max_second(self): self.assertEqual(max_of_three(3, 9, 5), 9)

    def test_max_third(self): self.assertEqual(max_of_three(3, 5, 9), 9)

    def test_two_equal_max(self): self.assertEqual(max_of_three(5, 9, 9), 9)

    def test_all_equal(self): self.assertEqual(max_of_three(7, 7, 7), 7)

    def test_negative_numbers(self): self.assertEqual(max_of_three(-1, -5, -3), -1)

    def test_floats(self): self.assertEqual(max_of_three(1.2, 3.4, 2.2), 3.4)

    def test_mixed_int_float(self): self.assertEqual(max_of_three(3, 4.5, 2), 4.5)

    def test_booleans(self): self.assertEqual(max_of_three(True, False, True), True)

    def test_large_small_mix(self): self.assertEqual(max_of_three(-1e9, 1e-9, 1e9), 1e9)

    def test_string_inputs(self): self.assertEqual(max_of_three("apple", "banana", "cherry"), "cherry")

