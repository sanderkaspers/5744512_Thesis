import unittest
from datasets.GPT_4.Few_shot.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(dif_Square(5), True) # Difference of squares (3^2 - 2^2))

    def test_case_2(self):
        self.assertEqual(dif_Square(4), True) # Difference of squares (2^2 - 0^2))

    def test_case_3(self):
        self.assertEqual(dif_Square(2), False) # Not a difference of squares)

    def test_case_4(self):
        self.assertEqual(dif_Square(1), True) # Difference of squares (1^2 - 0^2))

    def test_case_5(self):
        self.assertEqual(dif_Square(0), True) # Difference of squares (0^2 - 0^2))

    def test_case_6(self):
        self.assertEqual(dif_Square(-4), True) # Difference of squares (-2^2 - 0^2))

    def test_case_7(self):
        self.assertEqual(dif_Square(10), True) # Difference of squares (6^2 - 4^2))

    def test_case_8(self):
        self.assertEqual(dif_Square(14), False) # Not a difference of squares)

