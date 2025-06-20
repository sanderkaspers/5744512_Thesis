import unittest
from datasets.GPT_4.Zero_shot1.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_2(self):
        self.assertEqual(count([0, 0, 0]), 0)

    def test_3(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_4(self):
        self.assertEqual(count([10]), 10)

    def test_5(self):
        self.assertEqual(count([]), 0)

    def test_6(self):
        self.assertEqual(count([1.5, 2.5]), 4.0)

    def test_7(self):
        self.assertEqual(count([1, 2.5]), 3.5)

    def test_7(self):
        self.assertEqual(count([True, False, True]), 2)

