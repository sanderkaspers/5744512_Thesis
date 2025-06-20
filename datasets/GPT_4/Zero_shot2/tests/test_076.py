import unittest
from datasets.GPT_4.Zero_shot2.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_hex_1(self):
        self.assertEqual(hexagonal_num(1), 1)

    def test_hex_2(self):
        self.assertEqual(hexagonal_num(2), 6)

    def test_hex_3(self):
        self.assertEqual(hexagonal_num(3), 15)

    def test_hex_4(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_hex_5(self):
        self.assertEqual(hexagonal_num(-1), -3)

    def test_hex_6(self):
        self.assertEqual(hexagonal_num(100), 19701)

