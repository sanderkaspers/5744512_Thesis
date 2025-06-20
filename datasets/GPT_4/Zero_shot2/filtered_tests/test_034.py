import unittest
from datasets.GPT_4.Zero_shot2.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_hex_1(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_hex_2(self):
        self.assertEqual(centered_hexagonal_number(1), 1)

    def test_hex_3(self):
        self.assertEqual(centered_hexagonal_number(2), 7)

    def test_hex_4(self):
        self.assertEqual(centered_hexagonal_number(3), 19)

    def test_hex_5(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

    def test_hex_6(self):
        self.assertEqual(centered_hexagonal_number(-1), 7)

    def test_hex_7(self):
        self.assertEqual(centered_hexagonal_number(1000), 2997001)

