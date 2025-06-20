import unittest
from datasets.GPT_4.Zero_shot2.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_dif_1(self):
        self.assertTrue(dif_Square(0))

    def test_dif_2(self):
        self.assertTrue(dif_Square(1))

    def test_dif_3(self):
        self.assertFalse(dif_Square(2))

    def test_dif_4(self):
        self.assertTrue(dif_Square(3))

    def test_dif_5(self):
        self.assertTrue(dif_Square(-1))

    def test_dif_6(self):
        self.assertFalse(dif_Square(-2))

    def test_dif_7(self):
        self.assertTrue(dif_Square(-3))

    def test_dif_8(self):
        self.assertTrue(dif_Square(-4))

