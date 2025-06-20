import unittest
from datasets.GPT_4.Zero_shot2.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_smallest_1(self):
        self.assertEqual(smallest_num([4, 2, 9, 1]), 1)

    def test_smallest_2(self):
        self.assertEqual(smallest_num([-5, 3, -2]), -5)

    def test_smallest_3(self):
        self.assertEqual(smallest_num([7, 7, 7]), 7)

    def test_smallest_4(self):
        self.assertEqual(smallest_num([10]), 10)

    def test_smallest_5(self):
        self.assertEqual(smallest_num([-10, -20, -3]), -20)

