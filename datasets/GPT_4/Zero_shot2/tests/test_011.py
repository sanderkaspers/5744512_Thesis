import unittest
from datasets.GPT_4.Zero_shot2.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_signs_1(self):
        self.assertTrue(opposite_Signs(5, -10))

    def test_signs_2(self):
        self.assertTrue(opposite_Signs(-3, 8))

    def test_signs_3(self):
        self.assertFalse(opposite_Signs(3, 2))

    def test_signs_4(self):
        self.assertFalse(opposite_Signs(-4, -7))

    def test_signs_5(self):
        self.assertFalse(opposite_Signs(0, 5))

    def test_signs_6(self):
        self.assertFalse(opposite_Signs(0, -5))

    def test_signs_7(self):
        self.assertFalse(opposite_Signs(0, 0))

