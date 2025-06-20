import unittest
from datasets.GPT_4.Zero_shot1.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decimal_to_binary(10), '0b1010')

    def test_2(self):
        self.assertEqual(decimal_to_binary(0), '0b0')

    def test_3(self):
        self.assertEqual(decimal_to_binary(-10), '-0b1010')

    def test_4(self):
        self.assertTrue(decimal_to_binary(1024).startswith('0b'))

    def test_5(self):
        self.assertTrue(decimal_to_binary(-2048).startswith('-0b'))

    def test_6(self):
        self.assertEqual(decimal_to_binary(10), '0b1010')

    def test_7(self):
        self.assertEqual(decimal_to_binary(999), '0b1111100111')

    def test_8(self):
        self.assertEqual(decimal_to_binary(1), '0b1')

    def test_9(self):
        self.assertEqual(decimal_to_binary(True), '0b1')

    def test_10(self):
        self.assertEqual(decimal_to_binary(False), '0b0')

    def test_11(self):
        result = decimal_to_binary(2**100)
        self.assertTrue(result.startswith('0b'))

    def test_12(self):
        self.assertEqual(decimal_to_binary(2 + 2), '0b100')

    def test_13(self):
        self.assertEqual(decimal_to_binary(int("0xA", 16)), '0b1010')

    def test_14(self):
        self.assertEqual(decimal_to_binary(-1), '-0b1')

    def test_15(self):
        self.assertIsInstance(decimal_to_binary(10), str)

