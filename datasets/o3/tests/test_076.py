import unittest
from datasets.o3.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_first_hexagonal_number(self):
        self.assertEqual(hexagonal_num(1), 1)

    def test_general_value(self):
        self.assertEqual(hexagonal_num(3), 15)

    def test_zero_input(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_negative_input(self):
        self.assertEqual(hexagonal_num(-2), 10)

    def test_large_input(self):
        self.assertEqual(hexagonal_num(100), 19900)

