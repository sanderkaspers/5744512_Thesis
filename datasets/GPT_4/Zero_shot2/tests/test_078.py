import unittest
from datasets.GPT_4.Zero_shot2.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_pow_1(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(3))

    def test_pow_2(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(4))

    def test_pow_3(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(0))

    def test_pow_4(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(-3))

    def test_pow_5(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-2))

    def test_pow_6(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(999))

    def test_pow_7(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1000))

