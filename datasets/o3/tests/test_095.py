import unittest
from datasets.o3.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_integer_side(self):
        self.assertEqual(perimeter_pentagon(4), 20)

    def test_float_side(self):
        self.assertAlmostEqual(perimeter_pentagon(2.5), 12.5)

    def test_negative_side(self):
        self.assertEqual(perimeter_pentagon(-3), -15)

