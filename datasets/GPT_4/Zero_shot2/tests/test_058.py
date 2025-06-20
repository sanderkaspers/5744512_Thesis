import unittest
from datasets.GPT_4.Zero_shot2.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_check_1(self):
        self.assertTrue(check_integer("123"))

    def test_check_2(self):
        self.assertTrue(check_integer("-456"))

    def test_check_3(self):
        self.assertTrue(check_integer("  789  "))

    def test_check_4(self):
        self.assertFalse(check_integer("-"))

    def test_check_5(self):
        self.assertFalse(check_integer("abc"))

    def test_check_6(self):
        self.assertFalse(check_integer("12a3"))

    def test_check_7(self):
        self.assertFalse(check_integer(""))

    def test_check_8(self):
        self.assertFalse(check_integer("+123"))

    def test_check_9(self):
        self.assertFalse(check_integer("12 3"))

    def test_check_10(self):
        self.assertTrue(check_integer("00123"))

