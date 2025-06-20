import unittest
from datasets.GPT_4.Zero_shot1.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertTrue(check_integer("123"))

    def test_2(self):
        self.assertTrue(check_integer(" 123"))

    def test_3(self):
        self.assertTrue(check_integer("123 "))

    def test_4(self):
        self.assertTrue(check_integer(" 123 "))

    def test_5(self):
        self.assertFalse(check_integer(""))

    def test_6(self):
        self.assertFalse(check_integer("   "))

    def test_7(self):
        self.assertFalse(check_integer("abc"))

    def test_8(self):
        self.assertFalse(check_integer("123abc"))

    def test_9(self):
        self.assertFalse(check_integer("-123"))

    def test_10(self):
        self.assertFalse(check_integer("123.45"))

    def test_11(self):
        self.assertTrue(check_integer("0"))

    def test_12(self):
        self.assertFalse(check_integer("12\n"))

    def test_13(self):
        self.assertFalse(check_integer("123!"))

    def test_14(self):
        self.assertTrue(check_integer("\u0661\u0662\u0663"))

    def test_15(self):
        self.assertFalse(check_integer("1,000"))

    def test_16(self):
        self.assertFalse(check_integer("12e3"))

    def test_17(self):
        self.assertIsInstance(check_integer("456"), bool)

    def test_18(self):
        self.assertTrue(check_integer("9" * 1000))

