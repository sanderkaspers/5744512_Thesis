import unittest
from datasets.GPT_4.Zero_shot2.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_diff_1(self):
        self.assertTrue(is_Diff(22))

    def test_diff_2(self):
        self.assertFalse(is_Diff(23))

    def test_diff_3(self):
        self.assertTrue(is_Diff(-33))

    def test_diff_4(self):
        self.assertFalse(is_Diff(-32))

    def test_diff_5(self):
        self.assertTrue(is_Diff(0))

    def test_diff_6(self):
        self.assertTrue(is_Diff(1100))

    def test_diff_7(self):
        self.assertFalse(is_Diff(1101))

