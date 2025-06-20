import unittest
from datasets.GPT_4.Zero_shot2.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_pos_1(self):
        self.assertEqual(count_char_position("a1b2c3"), 2)

    def test_pos_2(self):
        self.assertEqual(count_char_position("123456"), 0)

    def test_pos_3(self):
        self.assertEqual(count_char_position(""), 0)

    def test_pos_4(self):
        self.assertEqual(count_char_position("abcdef"), 3)

    def test_pos_5(self):
        self.assertEqual(count_char_position("!@#$%^"), 0)

    def test_pos_6(self):
        self.assertEqual(count_char_position("A1B2C3"), 2)

    def test_pos_7(self):
        self.assertEqual(count_char_position("a"), 1)

    def test_pos_8(self):
        self.assertEqual(count_char_position("a b c"), 2)

    def test_pos_9(self):
        self.assertEqual(count_char_position("a1b1c1d1e1f1g1h1i1j1"), 5)

    def test_pos_10(self):
        self.assertEqual(count_char_position("a" * 1000), 500)

