import unittest
from datasets.GPT_4.Zero_shot1.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_woodall(23), True)

    def test_2(self):
        self.assertEqual(is_woodall(47), True)

    def test_3(self):
        self.assertEqual(is_woodall(15), False)

    def test_4(self):
        self.assertEqual(is_woodall(0), False)

    def test_5(self):
        self.assertEqual(is_woodall(1), False)

    def test_6(self):
        self.assertEqual(is_woodall(63), False)

    def test_7(self):
        self.assertEqual(is_woodall(191), True)

    def test_8(self):
        self.assertEqual(is_woodall(511), True)

    def test_9(self):
        self.assertEqual(is_woodall(1023), False)

