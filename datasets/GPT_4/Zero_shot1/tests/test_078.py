import unittest
from datasets.GPT_4.Zero_shot1.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(3))

    def test_2(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_3(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(-2))

    def test_4(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-3))

    def test_5(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(100000))

    def test_6(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(True))

    def test_7(self):
        self.assertIsInstance(is_Sum_Of_Powers_Of_Two(2), bool)

