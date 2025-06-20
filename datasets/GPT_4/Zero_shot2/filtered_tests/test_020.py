import unittest
from datasets.GPT_4.Zero_shot2.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_mono_1(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4]))

    def test_mono_2(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2]))

    def test_mono_3(self):
        self.assertTrue(is_Monotonic([3, 3, 3, 3]))

    def test_mono_4(self):
        self.assertFalse(is_Monotonic([1, 3, 2]))

    def test_mono_5(self):
        self.assertTrue(is_Monotonic([7]))

    def test_mono_6(self):
        self.assertTrue(is_Monotonic([2, 3]))

    def test_mono_7(self):
        self.assertTrue(is_Monotonic([3, 2]))

    def test_mono_8(self):
        self.assertTrue(is_Monotonic([]))

