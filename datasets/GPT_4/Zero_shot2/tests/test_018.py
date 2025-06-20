import unittest
from datasets.GPT_4.Zero_shot2.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_pos_1(self):
        self.assertEqual(pos_count([1, 2, 3]), 3)

    def test_pos_2(self):
        self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_pos_3(self):
        self.assertEqual(pos_count([-1, 0, 1]), 1)

    def test_pos_4(self):
        self.assertEqual(pos_count([0, 0, 0]), 0)

    def test_pos_5(self):
        self.assertEqual(pos_count([0, 1]), 1)

    def test_pos_6(self):
        self.assertEqual(pos_count([0, -1]), 0)

    def test_pos_7(self):
        self.assertEqual(pos_count([]), 0)

    def test_pos_8(self):
        self.assertEqual(pos_count([-5]), 0)

