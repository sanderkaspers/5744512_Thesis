import unittest
from datasets.GPT_4.Zero_shot2.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_bin_1(self):
        self.assertEqual(decimal_to_binary(5), '101')

    def test_bin_2(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_bin_3(self):
        self.assertEqual(decimal_to_binary(1), '1')

    def test_bin_4(self):
        self.assertEqual(decimal_to_binary(8), '1000')

    def test_bin_5(self):
        self.assertEqual(decimal_to_binary(7), '111')

    def test_bin_6(self):
        self.assertEqual(decimal_to_binary(6), '110')

    def test_bin_7(self):
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_bin_8(self):
        self.assertEqual(decimal_to_binary(2**31 - 1), bin(2**31 - 1)[2:])

    def test_bin_9(self):
        self.assertEqual(decimal_to_binary(-1), bin(-1).replace("0b", ""))

    def test_bin_10(self):
        self.assertEqual(decimal_to_binary(-8), bin(-8).replace("0b", ""))

    def test_bin_11(self):
        self.assertEqual(decimal_to_binary(10), '1010')

    def test_bin_12(self):
        self.assertEqual(decimal_to_binary(15), '1111')

    def test_bin_13(self):
        self.assertEqual(decimal_to_binary(32), '100000')

    def test_bin_14(self):
        self.assertEqual(decimal_to_binary(True), '1')

    def test_bin_15(self):
        self.assertEqual(decimal_to_binary(False), '0')

