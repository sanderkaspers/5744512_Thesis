import unittest
from datasets.GPT_4.Zero_shot1.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_Volume(0, 10, 10), 0)

    def test_2(self):
        self.assertEqual(find_Volume(5, 5, 5), 125)

    def test_3(self):
        self.assertEqual(find_Volume(100, 0, 100), 0)

    def test_4(self):
        self.assertEqual(find_Volume(2.5, 4, 2), 20.0)

    def test_5(self):
        self.assertEqual(find_Volume(3.3, 3.3, 3.3), 35.937)

    def test_6(self):
        self.assertEqual(find_Volume(1.5, 1.5, 1.5), 3.375)

    def test_7(self):
        self.assertEqual(find_Volume(-2, 3, 4), -24)

    def test_8(self):
        self.assertEqual(find_Volume(1e2, 1e2, 1e2), 1000000.0)

    def test_9(self):
        self.assertEqual(find_Volume(1, 1, 1), 1)

