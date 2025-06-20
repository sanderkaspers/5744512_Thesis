import unittest
from datasets.GPT_4.Zero_shot1.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_Monotonic([4, 3, 2, 1]), True)

    def test_2(self):
        self.assertEqual(is_Monotonic([1, 1, 1, 1]), True)

    def test_3(self):
        self.assertEqual(is_Monotonic([1, 3, 2]), False)

    def test_4(self):
        self.assertEqual(is_Monotonic([5]), True)

    def test_5(self):
        self.assertEqual(is_Monotonic([]), True)

    def test_6(self):
        self.assertEqual(is_Monotonic([1, 1, 2]), True)

    def test_7(self):
        self.assertEqual(is_Monotonic([1, 2, 2]), True)

    def test_8(self):
        self.assertEqual(is_Monotonic([3, 3, 2]), True)

    def test_9(self):
        self.assertEqual(is_Monotonic([3, 2, 2]), True)

