import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(square_perimeter(5), 20)

    def test_positive_float(self): self.assertEqual(square_perimeter(2.5), 10.0)

    def test_side_length_one(self): self.assertEqual(square_perimeter(1), 4)

    def test_large_input(self): self.assertEqual(square_perimeter(10**6), 4000000)

    def test_zero_input(self): self.assertEqual(square_perimeter(0), 0)

    def test_negative_input(self): self.assertEqual(square_perimeter(-4), -16)

