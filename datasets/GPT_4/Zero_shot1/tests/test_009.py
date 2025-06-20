import unittest
from datasets.GPT_4.Zero_shot1.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rev(100), 1)

    def test_2(self):
        self.assertEqual(rev(1), 1)

    def test_3(self):
        self.assertEqual(rev(0), 0)

    def test_4(self):
        self.assertEqual(rev(111), 111)

    def test_5(self):
        self.assertEqual(rev(9009), 9009)

    def test_6(self):
        self.assertEqual(rev(10), 1)

    def test_7(self):
        self.assertEqual(rev(1010), 101)

    def test_8(self):
        self.assertEqual(rev(987654321), 123456789)

    def test_9(self):
        self.assertEqual(rev(50005000), 550005)

