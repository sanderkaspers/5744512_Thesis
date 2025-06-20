import unittest
from datasets.GPT_4.Zero_shot2.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_count_1(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_count_2(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_count_3(self):
        self.assertEqual(count([1, -1, 2, -2]), 0)

    def test_count_4(self):
        self.assertEqual(count([]), 0)

    def test_count_5(self):
        self.assertEqual(count([0, 0, 0]), 0)

    def test_count_6(self):
        self.assertAlmostEqual(count([1.5, 2.5]), 4.0)

