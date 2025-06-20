import unittest
from datasets.GPT_4.Zero_shot1.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_2(self):
        self.assertEqual(pos_count([1, -1, 0]), 1)

    def test_3(self):
        self.assertEqual(pos_count([0, 0, 0]), 0)

    def test_4(self):
        self.assertEqual(pos_count([]), 0)

    def test_5(self):
        self.assertEqual(pos_count([1.1, 2.2, -3.3]), 2)

    def test_6(self):
        self.assertEqual(pos_count([0.0]), 0)

    def test_7(self):
        self.assertEqual(pos_count([10]), 1)

    def test_8(self):
        self.assertEqual(pos_count([-10]), 0)

