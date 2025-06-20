import unittest
from datasets.GPT_4.Zero_shot1.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum(1, 5), 10)

    def test_2(self):
        self.assertEqual(sum(3, 3), 0)

    def test_3(self):
        self.assertEqual(sum(5, 2), 0)

    def test_4(self):
        self.assertEqual(sum(-3, 3), 0)

    def test_5(self):
        self.assertEqual(sum(-5, -2), -12)

    def test_6(self):
        self.assertEqual(sum(1, 1001), 500500)

    def test_7(self):
        self.assertEqual(sum(-2, -2), 0)

