import unittest
from datasets.GPT_4.Few_shot2.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_square_perimeter_normal_value(self): self.assertEqual(square_perimeter(5), 20)

    def test_square_perimeter_zero(self): self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_negative_value(self): self.assertEqual(square_perimeter(-3), -12)

    def test_square_perimeter_float_value(self): self.assertEqual(square_perimeter(2.5), 10.0)

    def test_square_perimeter_large_number(self): self.assertEqual(square_perimeter(1000000), 4000000)

    def test_square_perimeter_very_small_number(self): self.assertEqual(square_perimeter(0.0001), 0.0004)

