import unittest
from datasets.GPT_4.Zero_shot1.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_difference([-1, -2, -3]), 2)

    def test_2(self):
        self.assertEqual(max_difference([-10, 0, 10]), 20)

    def test_3(self):
        self.assertEqual(max_difference([5, 5, 5]), 0)

    def test_4(self):
        self.assertEqual(max_difference([7]), 0)

    def test_5(self):
        self.assertEqual(max_difference([100, 200]), 100)

    def test_6(self):
        self.assertEqual(max_difference([-1000, 1000]), 2000)

    def test_7(self):
        self.assertEqual(max_difference([1.5, 2.5, -1.0]), 3.5)

