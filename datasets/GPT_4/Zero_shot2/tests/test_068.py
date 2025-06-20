import unittest
from datasets.GPT_4.Zero_shot2.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_sum_1(self):
        self.assertEqual(sum(1, 5), 15)

    def test_sum_2(self):
        self.assertEqual(sum(3, 3), 3)

    def test_sum_3(self):
        self.assertEqual(sum(5, 3), 0)

    def test_sum_4(self):
        self.assertEqual(sum(-3, 3), 0)

    def test_sum_5(self):
        self.assertEqual(sum(0, 4), 10)

    def test_sum_6(self):
        self.assertEqual(sum(-5, -1), -15)

    def test_sum_7(self):
        self.assertEqual(sum(1, 1000), 500500)

