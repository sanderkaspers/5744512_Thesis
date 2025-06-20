import unittest
from datasets.mbpp.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_square_perimeter_with_10_expect_40(self):
        self.assertEqual(square_perimeter(10), 40)

    def test_square_perimeter_with_5_expect_20(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_perimeter_with_4_expect_16(self):
        self.assertEqual(square_perimeter(4), 16)

