import unittest
from datasets.GPT_4.Zero_shot2.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_und_1(self):
        self.assertTrue(is_undulating(121))

    def test_und_2(self):
        self.assertTrue(is_undulating(2323))

    def test_und_3(self):
        self.assertFalse(is_undulating(12))

    def test_und_4(self):
        self.assertFalse(is_undulating(111))

    def test_und_5(self):
        self.assertFalse(is_undulating(123))

    def test_und_6(self):
        self.assertTrue(is_undulating(78787878))

    def test_und_7(self):
        self.assertFalse(is_undulating(777))

    def test_und_8(self):
        self.assertTrue(is_undulating(909090))

    def test_und_9(self):
        self.assertFalse(is_undulating(123123))

    def test_und_10(self):
        self.assertFalse(is_undulating(99999))

    def test_und_11(self):
        self.assertTrue(is_undulating(1010101))

    def test_und_12(self):
        self.assertTrue(is_undulating(int("10"*50)))

    def test_und_13(self):
        self.assertFalse(is_undulating(1213))

    def test_und_14(self):
        self.assertFalse(is_undulating(112112))

