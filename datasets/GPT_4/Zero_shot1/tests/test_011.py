import unittest
from datasets.GPT_4.Zero_shot1.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(opposite_Signs(-10, 20), True)

    def test_2(self):
        self.assertEqual(opposite_Signs(5, 8), False)

    def test_3(self):
        self.assertEqual(opposite_Signs(-5, -9), False)

    def test_4(self):
        self.assertEqual(opposite_Signs(0, -1), False)

    def test_6(self):
        self.assertEqual(opposite_Signs(0, 10), False)

