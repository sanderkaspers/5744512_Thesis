import unittest
from datasets.GPT_4.Zero_shot2.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_woodall_1(self):
        self.assertTrue(is_woodall(1))

    def test_woodall_2(self):
        self.assertTrue(is_woodall(23))

    def test_woodall_3(self):
        self.assertFalse(is_woodall(0))

    def test_woodall_4(self):
        self.assertFalse(is_woodall(10))

    def test_woodall_5(self):
        self.assertFalse(is_woodall(-5))

    def test_woodall_6(self):
        self.assertFalse(is_woodall(1000001))

