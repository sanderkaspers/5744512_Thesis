import unittest
from datasets.GPT_4.Zero_shot1.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_series(2), 2)

    def test_2(self):
        self.assertEqual(sum_series(3), 4)

    def test_3(self):
        self.assertEqual(sum_series(0), 0)

    def test_4(self):
        self.assertEqual(sum_series(-1), 0)

    def test_5(self):
        self.assertEqual(sum_series(10), 30)

    def test_6(self):
        self.assertEqual(sum_series(11), 36)

    def test_7(self):
        self.assertIsInstance(sum_series(5), int)

