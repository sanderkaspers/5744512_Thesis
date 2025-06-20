import unittest
from datasets.GPT_4.Zero_shot2.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_kth_1(self):
        self.assertEqual(kth_element([10, 20, 30], 1), 20)

    def test_kth_2(self):
        self.assertEqual(kth_element([10, 20, 30], 0), 10)

    def test_kth_3(self):
        self.assertEqual(kth_element([10, 20, 30], 2), 30)

    def test_kth_4(self):
        self.assertIsNone(kth_element([10, 20, 30], 3))

    def test_kth_5(self):
        self.assertIsNone(kth_element([], 0))

    def test_kth_6(self):
        self.assertIsNone(kth_element([10, 20, 30], -1))

