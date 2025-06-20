import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_typical_case_representable(self):
        self.assertTrue(dif_Square(9))  # 9 = 5^2 - 4^2

    def test_typical_case_not_representable(self):
        self.assertFalse(dif_Square(14))  # 14 % 4 == 2

    def test_negative_number(self):
        self.assertTrue(dif_Square(-7))  # Negative numbers return True

    def test_zero(self):
        self.assertTrue(dif_Square(0))  # 0 = 0^2 - 0^2

    def test_even_multiple_of_4(self):
        self.assertTrue(dif_Square(16))  # 16 = 9^2 - 7^2

    def test_even_remainder_2(self):
        self.assertFalse(dif_Square(18))  # 18 % 4 == 2

    def test_odd_number(self):
        self.assertTrue(dif_Square(7))  # 7 = 4^2 - 3^2

    def test_large_number(self):
        self.assertTrue(dif_Square(1000000003))  # Large prime number

    def test_floating_point_number(self):
        with self.assertRaises(TypeError):
            dif_Square(2.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            dif_Square('10')

