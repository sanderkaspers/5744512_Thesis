import unittest
from datasets.GPT_4.Zero_shot2.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_div_1(self):
        self.assertEqual(div_sum(7), 1)

    def test_div_2(self):
        self.assertEqual(div_sum(6), 6)

    def test_div_3(self):
        self.assertEqual(div_sum(12), 16)

    def test_div_4(self):
        self.assertEqual(div_sum(9), 4)

    def test_div_5(self):
        self.assertEqual(div_sum(1), 1)

    def test_div_6(self):
        self.assertEqual(div_sum(8), 7)

    def test_div_7(self):
        self.assertEqual(div_sum(15), 9)

    def test_div_8(self):
        self.assertEqual(div_sum(100), 117)

    def test_div_9(self):
        self.assertEqual(div_sum(-10), 1)

    def test_div_10(self):
        self.assertEqual(div_sum(0), 1)

