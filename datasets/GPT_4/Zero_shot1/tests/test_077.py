import unittest
from datasets.GPT_4.Zero_shot1.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(zero_count([1, 2, 3]), 0.0)

    def test_2(self):
        self.assertEqual(zero_count([0, 5]), 1.0)

    def test_3(self):
        self.assertEqual(zero_count([0.0, 2.5]), 1.0)

    def test_4(self):
        self.assertEqual(zero_count([0.0, 0, 3]), 2 / 1)

    def test_5(self):
        from array import array
        self.assertEqual(zero_count(array('i', [0, 1, 0])), 2 / 1)

    def test_6(self):
        self.assertEqual(zero_count([0, 2, 2.0, 0.0]), 2 / 2)

    def test_7(self):
        self.assertIsInstance(zero_count([0, 1]), float)

