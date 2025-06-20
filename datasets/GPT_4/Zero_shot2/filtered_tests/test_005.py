import unittest
from datasets.GPT_4.Zero_shot2.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_perimeter_1(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_perimeter_2(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_perimeter_3(self):
        self.assertEqual(square_perimeter(-3), -12)

    def test_perimeter_4(self):
        self.assertAlmostEqual(square_perimeter(2.5), 10.0)

    def test_perimeter_5(self):
        self.assertEqual(square_perimeter(1e6), 4e6)

    def test_perimeter_6(self):
        self.assertAlmostEqual(square_perimeter(0.0001), 0.0004)

