import unittest
from datasets.GPT_4.Zero_shot1.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(smallest_num([-1, -5, -3]), -5)

    def test_2(self):
        self.assertEqual(smallest_num([0, -1, 1]), -1)

    def test_3(self):
        self.assertEqual(smallest_num([5, 5, 5]), 5)

    def test_4(self):
        self.assertEqual(smallest_num([42]), 42)

    def test_5(self):
        self.assertEqual(smallest_num([3.1, 2.9, 4.5]), 2.9)

    def test_6(self):
        self.assertEqual(smallest_num([100, 50, 50, 100]), 50)

