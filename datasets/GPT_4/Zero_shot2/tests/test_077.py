import unittest
from datasets.GPT_4.Zero_shot2.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_zero_1(self):
        self.assertEqual(zero_count([0, 1, 2, 0, 3]), 2)

    def test_zero_2(self):
        self.assertEqual(zero_count([1, 2, 3]), 0)

    def test_zero_3(self):
        self.assertEqual(zero_count([]), 0)

    def test_zero_4(self):
        self.assertEqual(zero_count([0, 0, 0]), 3)

    def test_zero_5(self):
        self.assertEqual(zero_count([0]), 1)

    def test_zero_6(self):
        self.assertEqual(zero_count([-1, 0, -2, 0]), 2)

    def test_zero_7(self):
        self.assertEqual(zero_count([5, 10, 15]), 0)

    def test_zero_8(self):
        self.assertEqual(zero_count([0]*1000 + [1]*1000), 1000)

