import unittest
from datasets.o3.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(closest_num(10), 9)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative(self):
        self.assertEqual(closest_num(-5), -6)

    def test_one(self):
        self.assertEqual(closest_num(1), 0)

    def test_large_number(self):
        self.assertEqual(closest_num(1000000), 999999)

